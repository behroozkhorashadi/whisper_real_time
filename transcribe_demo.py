#! python3.7

import argparse

from whisper_trascriber import WhisperRealtimeTranscript


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="medium", help="Model to use",
                        choices=["tiny", "base", "small", "medium", "large"])
    parser.add_argument("--energy_threshold", default=1000,
                        help="Energy level for mic to detect.", type=int)
    parser.add_argument("--record_timeout", default=2,
                        help="How real time the recording is in seconds.",
                        type=float)
    parser.add_argument("--phrase_timeout", default=3,
                        help="How much empty space between recordings before"
                        "we consider it a new line in the transcription.",
                             type=float)
    args = parser.parse_args()

    whisper_transcriber = WhisperRealtimeTranscript(
        args.model,
        args.record_timeout,
        args.energy_threshold,
        args.phrase_timeout)
    transciption_result = whisper_transcriber.start_transcript()
    for line in transciption_result:
        print(line)


if __name__ == "__main__":
    main()
