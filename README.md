## 🔄 WAV から FLAC へのコンバーター

このスクリプトは、指定された入力ディレクトリ内（サブディレクトリを含む）のすべての `.wav` ファイルを `.flac` 形式に変換し、指定された出力ディレクトリに保存します。`ffmpeg` を使用しています。

### ⚙️ 必要環境

- **Python 3.x**
- **FFmpeg**（システムの PATH に追加されている必要があります）

> **Windows ユーザーへの注意：**  
> このスクリプトは `subprocess` を使用して `ffmpeg` を呼び出します。Linux や BSD ではネイティブに動作しますが、Windows 環境では `ffmpeg` の設定が正しくないと問題が発生する可能性があります。Windows 上で実行する場合は、Git Bash や WSL などの UNIX 互換シェルの使用を推奨します。

### 🚀 使い方

スクリプトを実行する前に、入力フォルダと出力フォルダを作成しておいてください。

```bash
python convert_wav_to_flac.py ./input_wavs ./output_flacs
