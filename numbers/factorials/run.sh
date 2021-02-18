#!/bin/bash

log()  { echo -e "\x1b[1m[\x1b[93mLOG\x1b[0m\x1b[1m]\x1b[0m ${@}";  }
info() { echo -e "\x1b[1m[\x1b[92mINFO\x1b[0m\x1b[1m]\x1b[0m ${@}"; }
warn() { echo -e "\x1b[1m[\x1b[91mWARN\x1b[0m\x1b[1m]\x1b[0m ${@}"; }

OUTDIR=factorials_lists/
APP=list_factorials.py
PREFIXNAME=factorials_

if [[ -d "${OUTDIR}" ]]; then rm -rf "${OUTDIR}"; fi
mkdir -p "${OUTDIR}"

info "Making list 1k"
python3 ${APP} ${OUTDIR}/${PREFIXNAME}1k.txt 1000

info "Making list 10k"
python3 ${APP} ${OUTDIR}/${PREFIXNAME}10k.txt 10000

info "Making list 100k"
python3 ${APP} ${OUTDIR}/${PREFIXNAME}100k.txt 100000

info "Making list 1M"
python3 ${APP} ${OUTDIR}/${PREFIXNAME}1M.txt 1000000
