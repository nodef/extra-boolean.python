#!/usr/bin/env bash

setupDeploy() {
git clone https://${GITHUB_TOKEN}@github.com/python3f/deploy "$HOME/deploy"
bash "$HOME/deploy/install.sh"
}

setupTest() {
pip install -U pytest
pip install .
if [[ -f "requirements.txt" ]]; then
  pip install -r requirements.txt
fi
}

deploy() {
bash "$HOME/deploy/script.sh"
}


if [[ "$1" != "deploy" ]]; then
  if [[ "$GITHUB_TOKEN" != "" ]]; then setupDeploy; else setupTest; fi
else
  if [[ -d "$HOME/deploy" ]]; then deploy; else pytest; fi
fi
