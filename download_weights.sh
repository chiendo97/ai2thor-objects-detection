gdrive_download () {
  CONFIRM=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://drive.google.com/uc?export=download&id=$1" -O- | sed -En 's/.*confirm=([0-9A-Za-z_]+).*/\1/p')
  wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$CONFIRM&id=$1" -O $2
  rm -f /tmp/cookies.txt
}
tar_download_and_extract() {
  rm -rf $1*
  gdrive_download $2 $1.tar.gz
  tar -zxvf $1.tar.gz
  rm -rf $1.tar.gz
}

tar_download_and_extract yolo_weights 1jBMYeZY7n_dkeRMqq1XDCXljqR6c70DP
