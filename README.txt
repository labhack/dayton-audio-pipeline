
Products of Dayton's [LabHack 2016](http://www.labhack.org/) team
for the [Audio Pipeline challenge](http://www.labhack.org/prizes/audio/)

Components:

- GUI for selecting and applying signal processing filters
- `transcribe/transcribe.py` for submitting audio files to third-party
API services to generarte text

Requirements:

- [Qt Creator](https://www.qt.io/ide/)
- [GNU Radio](http://gnuradio.org/) (install with `brew`)


Icky filenames (with spaces, special characters, etc) may trip up the
analysis scripts, and automatically recorded WAV files often have these
icky names.  The [detox](http://detox.sourceforge.net/) utility,
run recursively (`-r`), helps with this.
