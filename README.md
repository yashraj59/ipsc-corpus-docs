# iPSC Corpus Kit Documentation

Standalone Read the Docs project for `ipsc-corpus-kit`.

## Citation

If you use iPSC Corpus Kit, please cite:

```text
Yash Raj. (2026). iPSC Corpus Kit (Version 0.3.0) [Computer software].
GitHub. https://github.com/yashraj59/ipsc-corpus-kit
```

Machine-readable citation metadata is available in `CITATION.cff`.

## License

This documentation is released under the [MIT License](LICENSE). Source datasets
described by the documentation retain their own licenses and usage constraints.

Build locally:

```bash
cd /home/ubuntu/ipsc-corpus-docs
python -m pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` in a browser after the build.
