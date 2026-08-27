# C3-B1 project/license disposition review, round 1

- Reviewer: `c3-b1-project-license-reviewer-1` (`/root/c3_b1_legal_review`)
- Review date: `2026-08-26` (America/Los_Angeles)
- Governing contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` / `d9fb09345ab85580cd8c877745262d1b481e366f`
- Assignment commit/tree: `a4572ac584aabd6f6231e40ca65a45e0b9873154` / `eb43fde795e5c3b92a0ac69c0e9098914e4696cc`
- Review kind: engineering compliance disposition, not legal advice or a legal guarantee

## Scope and evidence identity

This review is limited to future inclusion of the following inert, checked-in
source bytes in the `pico-logic-analyzer` Python distribution. No decoder or
runner was imported or executed, no dependency was installed, and no package
was built or published.

| Repository source path | SHA-256 | Observed notice |
| --- | --- | --- |
| `Software/decoders/sigrokdecode.py` | `385124002ec16379a2542f2905c5ce41f3402032458d89f49617623ab7aaf01a` | No copyright or license notice in file |
| `Software/decoders/uart/__init__.py` | `351098a23f5caa205068688550af53bd44a63776e1d02921ba32487ce720b92f` | GPL-2.0-or-later; Uwe Hermann, 2012 |
| `Software/decoders/uart/pd.py` | `67655f53162c531bc6eb77d9d29b384edec80a2dd5bd741897b4aa2afc52ffcc` | GPL-2.0-or-later; Uwe Hermann, 2011-2014 |
| `Software/decoders/spi/__init__.py` | `91b207f82c59fe1c12ad1458ef669c4293c7e4c8dd19bec14e78b455305af56c` | GPL-2.0-or-later; Uwe Hermann, 2012 |
| `Software/decoders/spi/pd.py` | `ef9cac5098404dc164094712e9175ba3715233248d8bbc23cb85ed3fc51d5d3d` | GPL-2.0-or-later; Gareth McMullin, 2011; Uwe Hermann, 2012-2014 |
| `Software/decoders/i2c/__init__.py` | `37931874732ea0b3ca13784b8df4cd90949a2c1b5822feae5d5df6da81ee886f` | GPL-2.0-or-later; Uwe Hermann, 2012 |
| `Software/decoders/i2c/pd.py` | `b6899137fb5b505433e696d319b7f3cc88519b43e2a2e7fea1a9f770ba10a305` | GPL-2.0-or-later; Uwe Hermann, 2010-2016 |
| `Software/decoders/common/srdhelper/__init__.py` | `125b0616dfdd974c2f6e0e83e61cf9cdd21340f9ab11ac7b97b648792dad05d1` | GPL-2.0-or-later; Uwe Hermann, 2012-2014 |
| `Software/decoders/common/srdhelper/mod.py` | `602b27901820a27af5fcf317b34af1a17d1449fa1ad21279507d1d5ab8acebd6` | GPL-2.0-or-later; Uwe Hermann, 2012-2020 |

The accepted provenance inputs are
`docs/cycle-3-decoder-provenance-license.md` (SHA-256
`3155b8ea00e54fc8facd86d6a28604e9a0f3cf1097751392e6a12380ad9ddc4c`)
and `testdata/decoders/cycle3/provenance.json` (SHA-256
`e0a6082869cdf51e7abf74441065b080b8e1d6614a45ad52f034ef95f4f4c8e4`).
They bind import commit `407b5ef039aa0474c400c0721749baa126e53270`
and prior gitlink `Software/SigrokDecode` at
`0235970293590f673a253950e6c61017cefa97df`. The nine files entered their
current repository paths together at the import commit. The shim bytes are
identical to the predecessor
`Software/LogicAnalyzer/LogicAnalyzer/SigrokDecoderBridge/sigrokdecode.py`
before that import and are present in history from initial commit
`36fd732a52678b6e387c049389ad69c7e3551217`; that history does not manufacture
an absent in-file license notice.

Current Python metadata is bound by `Software/LogicAnalyzerPy/pyproject.toml`
SHA-256 `56f56100d48c9586ca49f14c77e84f23668e1af0670d548c22fca1db636061f2`:
it declares legacy `license = {text = "MIT"}`, declares no license files or
license classifiers, and currently packages only web assets. The repository
root `LICENSE`, SHA-256
`3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986`,
is the unmodified GNU GPL version 3 text.

## Authoritative factual basis

The eight marked files grant a choice of GPL version 2 or any later version.
The FSF explains that GPL-2.0-or-later code is compatible with GPLv3 because
version 3 is one of the permitted choices, and its compatibility table calls
the resulting combination GPLv3. This is the compatibility basis for selecting
`GPL-3.0-only` for the installed distribution, while leaving each upstream
file's broader GPL-2.0-or-later notice intact:
<https://www.gnu.org/licenses/gpl-faq.en.html#v2v3Compatibility>.
SPDX defines the component identifier `GPL-2.0-or-later` and distinguishes it
from GPL-2.0-only
(<https://spdx.org/licenses/GPL-2.0-or-later.html>), and defines
`GPL-3.0-only` for GNU GPL version 3 only
(<https://spdx.org/licenses/GPL-3.0-only.html>).

For modern project metadata, the PyPA `pyproject.toml` specification requires
the `license` string to be a valid SPDX expression, defines `license-files`,
and deprecates `License ::` classifiers:
<https://packaging.python.org/en/latest/specifications/pyproject-toml/#license>.
For Metadata 2.4 wheels, each `License-File` must be present under
`.dist-info/licenses/` at its declared relative path:
<https://packaging.python.org/en/latest/specifications/binary-distribution-format/#the-dist-info-licenses-directory>.
These are packaging facts. Whether this repository's particular ownership and
provenance are legally sufficient is a question for qualified counsel and
rights holders, not this engineering record.

## Required future disposition

Before any of these snapshots can enter an installed distribution, copy the
exact bytes, without editing their headers, into this private package-data
root:

`Software/LogicAnalyzerPy/src/pico_logic_analyzer/_decoder_snapshots/407b5ef039aa0474c400c0721749baa126e53270/`

The relative layout beneath it must be exactly `sigrokdecode.py`,
`uart/{__init__.py,pd.py}`, `spi/{__init__.py,pd.py}`,
`i2c/{__init__.py,pd.py}`, and
`common/srdhelper/{__init__.py,mod.py}`. The directory is private, excluded
from setuptools package discovery, unavailable as a supported public import,
and exposed only to the later closed, hash-checking worker. Placement must not
change any of the nine SHA-256 values.

Create `Software/LogicAnalyzerPy/ATTRIBUTION.md` as the package attribution
manifest. It must contain: all nine installed relative paths and digests; the
original repository paths; import commit and prior gitlink above; the exact
observed copyright names/year ranges from the table; `GPL-2.0-or-later` for
the eight marked files; `notice not present in file; project-history/rights
confirmation required` for the shim; a statement that source headers are
retained verbatim; the upstream libsigrokdecode project name and its canonical
project URL; and pointers to both included GPL texts. It must not label the
shim as upstream or invent an author/license.

Create these package-local license files before building:

- `Software/LogicAnalyzerPy/LICENSE`: byte-for-byte copy of the repository
  root GPLv3 text (the root file remains present and unchanged).
- `Software/LogicAnalyzerPy/LICENSES/GPL-2.0-or-later.txt`: complete official
  GNU GPL version 2 text corresponding to the retained component notices.
- `Software/LogicAnalyzerPy/LICENSES/MIT.txt`: complete MIT text covering the
  pre-existing MIT-labelled Python-package portions, after rights-holder review
  confirms that label and attribution. Including it preserves component
  licensing information; it does not change the distribution-level expression.

Change `[project]` in `pyproject.toml` exactly as follows: replace the legacy
table with `license = "GPL-3.0-only"`; add
`license-files = ["LICENSE", "LICENSES/GPL-2.0-or-later.txt", "LICENSES/MIT.txt", "ATTRIBUTION.md"]`;
do not add a deprecated `License ::` classifier. Keep `readme = "README.md"`,
but add a README licensing/provenance section that states the distribution
expression, identifies the GPL-2.0-or-later snapshot subset and private path,
links `ATTRIBUTION.md`, and makes no warranty or legal-certification claim.

Under `[tool.setuptools.packages.find]`, exclude
`pico_logic_analyzer._decoder_snapshots*`. Under
`[tool.setuptools.package-data]`, retain the existing web patterns and add the
five explicit patterns rooted at the full commit directory:
`_decoder_snapshots/407b5ef039aa0474c400c0721749baa126e53270/sigrokdecode.py`,
`.../uart/*.py`, `.../spi/*.py`, `.../i2c/*.py`, and
`.../common/srdhelper/*.py`. Do not use an unbounded decoder-tree glob and do
not package any other checked-in decoder.

## Mandatory pre-installation verification

A later authorized packaging gate must, in a clean Python 3.12 environment:

1. recompute all nine source and staged package-data digests and require the
   table above exactly, with no extra file under the private snapshot root;
2. statically verify all eight GPL headers remain byte-identical and that the
   attribution manifest contains every required field, including the shim
   caveat and confirmed project ownership/license disposition;
3. validate the SPDX expression and emitted core metadata, and require all four
   declared license/attribution files in sdist and in the wheel's
   `.dist-info/licenses/` tree;
4. inspect wheel and sdist file lists to require only the nine allowlisted
   snapshot files, then install the wheel into a fresh environment and inspect
   installed `RECORD`, resources, metadata, license files, CLI help, and the
   absence of a public snapshot import surface; and
5. rerun the project's authorized installed-package, provenance, prohibited-
   dependency, and non-hardware regression gates without using decoder output
   as an oracle.

No editable install may expose the snapshots before these source-side changes
and static checks are complete. No wheel, sdist, package build, upload,
publication, or distribution is authorized by this review now.

## Legal-counsel and rights-holder limitation

The engineering disposition is concrete and internally consistent, but it
cannot establish copyright ownership, provenance beyond the recorded history,
or authority to relicense project-authored portions. Before any conveyance,
qualified counsel or the relevant rights holders must confirm (a) the shim's
license/ownership despite its missing header, (b) the authority and attribution
behind the current MIT label, and (c) that the proposed combined-work treatment
fits the actual implementation and distribution. A negative or unavailable
confirmation keeps all builds and distribution prohibited; it must not be
converted into a pass by metadata alone.

## Findings

1. The present MIT-only metadata and absent package license/attribution files
   are not an acceptable metadata description for an installed distribution
   containing the eight GPL-2.0-or-later files. The future changes above are a
   mandatory precondition, not changes made by this review.
2. The shim's absent in-file notice is a provenance limitation. The mandatory
   manifest caveat and rights-holder/counsel confirmation prevent the review
   from silently assigning it a license.
3. The repository currently has unrelated untracked runner/method work. This
   reviewer neither inspected it as licensing evidence nor changed it.

pass
