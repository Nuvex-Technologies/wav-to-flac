# このスクリプトは指定されたディレクトリ内のすべての.wavファイルを
# 同じ構造のフォルダ階層で.flac形式に変換して保存します。
# FFmpegを使用して高圧縮レベルでエンコードを行います。
# 入力と出力のディレクトリはコマンドライン引数で指定します。

import os
import subprocess
from pathlib import Path

def convert_wav_to_flac(input_dir, output_dir):
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    if not input_path.is_dir():
        raise NotADirectoryError(f"Input directory not found: {input_path}")
    
    output_path.mkdir(parents=True, exist_ok=True)

    wav_files = list(input_path.rglob("*.wav"))

    if not wav_files:
        print("No .wav files found.")
        return

    for wav_file in wav_files:
        rel_path = wav_file.relative_to(input_path)
        flac_file = output_path / rel_path.with_suffix(".flac")
        flac_file.parent.mkdir(parents=True, exist_ok=True)

        cmd = [
            "ffmpeg",
            "-y",
            "-i", str(wav_file),
            "-compression_level", "12",
            str(flac_file)
        ]

        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Converted: {wav_file} → {flac_file}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to convert {wav_file}: {e.stderr.decode().strip()}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert all .wav files in a folder to .flac format.")
    parser.add_argument("input_folder", help="Path to the input folder containing .wav files")
    parser.add_argument("output_folder", help="Path to the output folder where .flac files will be saved")

    args = parser.parse_args()
    convert_wav_to_flac(args.input_folder, args.output_folder)
