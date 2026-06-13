#!/usr/bin/env python3
"""
verify_dois.py — prove the example's three papers are REAL, and that the
demo's whole point is grounded in fact, not in our retelling.

Synthesis Lab's promise is citation discipline: cite only real, supplied
papers, and never credit a paper with a finding it did not make. The trust
demo in examples/README.md hinges on one specific, checkable fact — that
**Karpicke & Roediger (2008) is about *retrieval practice*, not *spacing***,
which is exactly why a careful tool must NOT cite it for a spacing result.

This tiny script makes that checkable by anyone. For each of the three DOIs
cited in the example it asks the authoritative DOI registry directly — the
Crossref REST API (https://api.crossref.org/works/<doi>) — which returns the
real bibliographic record for a registered DOI and a 404 for one that was
never minted. On top of confirming all three are real, it asserts the
linchpin claim against live registry metadata: Karpicke & Roediger (2008)'s
registered title contains "retrieval" and does NOT contain "spacing". If the
demo had quietly mislabeled that paper, this check would fail.

Dependency-light by design: standard library only (urllib), no pip install.

    python examples/verify_dois.py

Exit code 0 = all three are real AND the retrieval-not-spacing claim holds.
Non-zero = at least one check failed.
"""
import json
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

# The exact DOIs cited in examples/README.md, with the role each plays in the
# demo. Order matches the references list there.
PAPERS = [
    ("10.1037/0033-2909.132.3.354", "Cepeda et al. 2006, Psychological Bulletin "
                                     "(the genuine spacing meta-analysis)"),
    ("10.1126/science.1152408",     "Karpicke & Roediger 2008, Science "
                                     "(retrieval practice — the trap paper)"),
    ("10.1002/acp.1537",            "Kornell 2009, Applied Cognitive Psychology "
                                     "(flashcards: spacing beats cramming)"),
]

# The linchpin of the whole demo: this paper is about retrieval, not spacing.
KARPICKE_DOI = "10.1126/science.1152408"

USER_AGENT = "academi-skill-verify/1.0 (+https://github.com/; mailto:hello@example.com)"
TIMEOUT = 30

# Some machines ship a broken/empty CA store, which makes HTTPS to these public
# read-only endpoints fail with CERTIFICATE_VERIFY_FAILED. Try verified first;
# fall back to unverified. These are public GETs, so the fallback is low-risk.
try:
    import certifi
    _CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    _CTX = ssl.create_default_context()
_CTX_UNVERIFIED = ssl._create_unverified_context()


def _open(url):
    """GET with a CA-store fallback. Returns the response object."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    last = None
    for ctx in (_CTX, _CTX_UNVERIFIED):
        try:
            return urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx)
        except urllib.error.URLError as e:
            reason = getattr(e, "reason", None)
            if isinstance(reason, ssl.SSLError) and ctx is _CTX:
                last = e
                continue
            raise
    raise last


def crossref_record(doi):
    """Return the Crossref message dict for a registered DOI, None if the DOI
    was never registered (404 — the fabrication case), or raises on other
    errors so the caller can report an inconclusive network result."""
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    try:
        with _open(url) as resp:
            if resp.getcode() == 200:
                return json.load(resp).get("message", {})
            return None
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def main():
    print(f"Verifying {len(PAPERS)} example DOIs against the Crossref registry ...\n")
    failures = 0
    karpicke_title = None

    for doi, role in PAPERS:
        try:
            rec = crossref_record(doi)
        except Exception as e:  # network / rate-limit — report, don't crash
            print(f"INCONCLUSIVE {doi}  ({role})\n    could not reach Crossref: {e}")
            failures += 1
            continue
        if rec is None:
            print(f"FAIL {doi}  not registered in Crossref (DOI does not exist)")
            failures += 1
            continue
        title = (rec.get("title") or ["?"])[0]
        authors = rec.get("author") or []
        first = authors[0].get("family", "?") if authors else "?"
        year = rec.get("issued", {}).get("date-parts", [[None]])[0][0]
        venue = (rec.get("container-title") or ["?"])[0]
        print(f"PASS {doi}  registered: {first} {year}, {venue}")
        print(f"     “{title}”")
        print(f"     role in demo: {role}")
        if doi == KARPICKE_DOI:
            karpicke_title = title.lower()

    # The claim the whole demo rests on, checked against live registry data.
    print("\nLinchpin claim — Karpicke & Roediger (2008) is about RETRIEVAL, "
          "not SPACING:")
    if karpicke_title is None:
        print("  COULD NOT CHECK (record not retrieved above).")
        failures += 1
    elif "retrieval" in karpicke_title and "spacing" not in karpicke_title:
        print("  PASS — registered title contains \"retrieval\" and not "
              "\"spacing\".")
        print("  So citing it for a *spacing* finding would be a miscredit — "
              "exactly what the demo shows the skill avoids.")
    else:
        print("  FAIL — the registered title did not match the expected "
              "retrieval-not-spacing pattern.")
        failures += 1

    print()
    if failures:
        print(f"{failures} check(s) failed.")
        sys.exit(1)
    print("All three papers are real, and the retrieval-not-spacing claim holds. "
          "The demo is grounded in fact.")
    sys.exit(0)


if __name__ == "__main__":
    main()
