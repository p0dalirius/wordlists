#!/bin/bash

log()  { echo -e "\x1b[1m[\x1b[93mLOG\x1b[0m\x1b[1m]\x1b[0m ${@}";  }
info() { echo -e "\x1b[1m[\x1b[92mINFO\x1b[0m\x1b[1m]\x1b[0m ${@}"; }
warn() { echo -e "\x1b[1m[\x1b[91mWARN\x1b[0m\x1b[1m]\x1b[0m ${@}"; }

OUTDIR=prime_factors_lists/
APP=list_prime_factors.py
PREFIXNAME=primefactors_

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

info "Making list 10M"
python3 ${APP} ${OUTDIR}/${PREFIXNAME}10M.txt 10000000

# info "Making list 100M"
# python3 ${APP} ${OUTDIR}/${PREFIXNAME}100M.txt 100000000
#
# info "Making list 1B"
# python3 ${APP} ${OUTDIR}/${PREFIXNAME}1B.txt 1000000000
