# OrcaCyber PHP2Shell: Defender Research Artifacts

Analysis of **CVE-2026-109618** and **CVE-2026-109619**. This package provides offline defensive tools and does **not** contain a working exploit, heap-spray request generator, address-layout bypass, or attack chain.

**Research attribution:** The project reports that the PoC was created with OrcaCyber Zero and OrcaCyber Ultra. The uploaded bundle also credits a public third-party exploit; accurately distinguish model-assisted work from original discovery.

## Scripts

```bash
python3 check_php_version.py 'PHP 8.4.26 (cli)'
python3 check_php_version.py 'PHP 8.4.27 (cli)'
python3 analyze_response_offline.py /path/to/captured-response.bin
python3 summarize_apache_crashes.py /path/to/apache-error.log
```

- `check_php_version.py`: classifies upstream release versions (not definitive for vendor-backported builds).
- `analyze_response_offline.py`: measures an already-captured `PHPSESSID` response header **without printing secrets**. It does not make requests.
- `summarize_apache_crashes.py`: counts Apache worker crash lines in existing logs. Not a vulnerability detector.

## Evidence that may be published

- Redacted worker crash logs and crash counts.
- Aggregate `PHPSESSID` encoded/decoded lengths, **not** the 2.3 MB raw response containing possible secrets.
- Sanitized account execution proof (the lab `www-data` result), with original-public-exploit attribution.
- Short root-cause explanation and links to official PHP patch, instead of copying a full repository diff.

## Fixed upstream versions

PHP 8.2.35, 8.3.36, 8.4.27, 8.5.12. Check distro package advisories for backports. Restart relevant workers after updating.

## References

- https://www.php.net/archive/2026.php#2026-10-21-5
- https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w
- https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp
- https://cert.europa.eu/publications/security-advisories/2026-018/
