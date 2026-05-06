# Audio Identification & Source Detection System

## Team Information
- **Team Name**: Code titans
- **Year**: 1st 
- **All-Female Team**: No

## Architecture Overview

#### Describe your approach here. Keep it short and clear.

    - We generate an MD5-based audio fingerprint from the raw audio bytes and extract spectrogram features like tempo, pitch, and energy level for each audio clip and store         them in a structured in-memory database for fast lookup.
    - We use fingerprint-based similarity matching combined with spectrogram feature comparison to identify the closest matching song from the database even for noisy or             partial audio inputs.
    - The system uses a modular design where the song database can be extended to thousands of entries. The fingerprint matching is O(n) and can be optimized with indexing            for larger datasets.
    - We use lightweight MD5 fingerprinting for speed and a confidence scoring system that accounts for noise levels in the input to ensure accurate results even with                distorted audio.

**Note:** Please do not change the format or spelling of anything in this README. The fields are extracted using a script, so any changes to the structure or formatting may break the extraction process.
