#!/usr/bin/env python3
"""DAX9 ROT007: source-only, bounded Mark II HEPData + independently SHA-pinned
Rivet-data RPM -> original packaged YODA receipt. No physics calculations.
Use from GitHub Actions; no hidden local or user credentials required.
"""
import gzip
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import urllib.request

OUT = pathlib.Path(os.environ.get("DAX_MARKII_SOURCE_OUT", "/tmp/dax-s9-rot007"))
OUT.mkdir(parents=True, exist_ok=True)
EXPECTED_RPM = "a5ca114950e3a75240d3ed8e7af21f27a26713d95a8ecba6ce0885e2bf6dd090"
URLS = [
    "https://mirror.umd.edu/opensuse/factory/repo/oss/noarch/Rivet-data-4.1.2-2.2.noarch.rpm",
    "https://www.ftp.fau.de/opensuse/factory/repo/oss/noarch/Rivet-data-4.1.2-2.2.noarch.rpm",
    "https://download.opensuse.org/slowroll/repo/oss/noarch/Rivet-data-4.1.2-2.2.noarch.rpm",
]
HEPDATA = {
    "native_table1_csv": "https://www.hepdata.net/download/table/ins304882/Table%201/csv",
    "native_submission_yoda": "https://www.hepdata.net/download/submission/ins304882/1/yoda",
}
RECEIPT = {
    "identity": "MARKII_1990_I304882",
    "source_record": "https://www.hepdata.net/record/ins304882",
    "rpm_advertised_sha256": EXPECTED_RPM,
    "rpm_checksum_source": "https://tumbleweed.opensuse.org/download/slowroll/repo/oss/noarch/Rivet-data-4.1.2-2.2.noarch.rpm.mirrorlist",
    "hepdata": {},
    "rpm": {},
    "packaged_reference": {},
}

def write_receipt():
    (OUT / "source_receipt.json").write_text(json.dumps(RECEIPT, sort_keys=True, indent=2) + "\n", encoding="utf-8")

for name, url in HEPDATA.items():
    entry = {"url": url, "status": "ACCESS_HOLD"}
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "NASH-DAX9-native-source-read-receipt/1.0", "Accept": "application/zip,text/csv,*/*"}
        )
        with urllib.request.urlopen(req, timeout=18) as resp:
            mime = resp.headers.get("Content-Type", "")
            data = resp.read(6000001)
        entry.update(mime=mime, bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        if len(data) > 6000000:
            entry["status"] = "REJECT_OVERSIZE"
        elif data.lstrip().lower().startswith((b"<html", b"<!doctype html")):
            entry["status"] = "REJECT_HTML"
        elif data.startswith(b"PK") or b"," in data[:200]:
            ext = ".zip" if data.startswith(b"PK") else ".csv"
            (OUT / (name + ext)).write_bytes(data)
            entry.update(status="ORIGINAL_BYTES_RECEIVED", stored_as=name + ext)
        else:
            entry["status"] = "REJECT_UNKNOWN_FORMAT"
    except Exception as e:
        entry["error"] = repr(e)
    RECEIPT["hepdata"][name] = entry
    print("HEPDATA_ORIGINAL", name, entry["status"], flush=True)

rpm = OUT / "Rivet-data-4.1.2-2.2.noarch.rpm"
for url in URLS:
    print("TRY_RPM", url, flush=True)
    tmp = OUT / "download.tmp"
    try:
        cmd = ["curl", "-L", "--fail", "--silent", "--show-error", "--retry", "1", "--max-time", "100",
               "--max-filesize", "55000000", url, "-o", str(tmp)]
        run = subprocess.run(cmd, capture_output=True, text=True, timeout=115)
        if run.returncode != 0:
            RECEIPT["rpm"].setdefault("attempts", []).append({"url": url, "status": "FETCH_FAILED", "stderr": run.stderr[-250:]})
            continue
        sha = hashlib.sha256(tmp.read_bytes()).hexdigest()
        if sha != EXPECTED_RPM:
            RECEIPT["rpm"].setdefault("attempts", []).append({"url": url, "status": "REJECT_CHECKSUM", "sha256": sha})
            continue
        tmp.rename(rpm)
        RECEIPT["rpm"].update(status="OFFICIAL_SHA256_MATCH", url=url, bytes=rpm.stat().st_size, sha256=sha)
        print("RPM_SHA_PASS", sha, flush=True)
        break
    except Exception as e:
        RECEIPT["rpm"].setdefault("attempts", []).append({"url": url, "status": "ACCESS_HOLD", "error": repr(e)})
    finally:
        if tmp.exists():
            tmp.unlink()
if not rpm.exists():
    RECEIPT["rpm"]["status"] = "ACCESS_HOLD"
else:
    dest = OUT / "rpm_extracted"
    dest.mkdir(exist_ok=True)
    # apt-installed rpm2cpio+cpio provided by workflow.
    target = "./usr/share/Rivet/MARKII_1990_I304882.yoda.gz"
    command = "set -euo pipefail; rpm2cpio " + str(rpm) + " | cpio --quiet -id '" + target + "'"
    p = subprocess.run(["bash", "-lc", command], cwd=dest, capture_output=True, text=True, timeout=60)
    yoda = dest / "usr/share/Rivet/MARKII_1990_I304882.yoda.gz"
    if p.returncode == 0 and yoda.exists():
        raw = yoda.read_bytes()
        data = gzip.decompress(raw)
        decoded = data.decode("utf-8")
        copy = OUT / "MARKII_1990_I304882.yoda.gz"
        copy.write_bytes(raw)
        names = re.findall(r"(?m)^BEGIN YODA_\S+\s+(\S+)", decoded)
        RECEIPT["packaged_reference"] = {
            "status": "AUTHENTIC_RIVET_PACKAGE_REFERENCE_BYTES",
            "sha256_compressed": hashlib.sha256(raw).hexdigest(),
            "compressed_bytes": len(raw),
            "uncompressed_bytes": len(data),
            "object_count": len(names),
            "object_ids": names[:35],
        }
        (OUT / "markii_source_head.txt").write_text("\n".join(decoded.splitlines()[:170]) + "\n")
        print("MARKII_YODA_SUCCESS", json.dumps(RECEIPT["packaged_reference"],sort_keys=True), flush=True)
    else:
        RECEIPT["packaged_reference"] = {"status": "EXTRACT_HOLD", "returncode": p.returncode, "stderr": p.stderr[-500:]}
    rpm.unlink()
write_receipt()
print("FINAL_SOURCE_RECEIPT", json.dumps({
    "hepdata": {k: v["status"] for k, v in RECEIPT["hepdata"].items()},
    "rpm": RECEIPT["rpm"].get("status"),
    "rivet": RECEIPT["packaged_reference"].get("status", "NOT_FETCHED")},sort_keys=True), flush=True)
