# ChatGPT-streamlit
使用Streamlit构建的易于使用的ChatGPT用户界面，可用于ChatGPT、Claude、Stable Diffusion等。

Easy to use ChatGPT UI built with Streamlit for using ChatGPT, Claude, Stable Diffusion and beyond.

![demo](figures/demo.png)

使用方法 (Usage):

1. `git clone https://github.com/zinccat/ChatGPT-streamlit`
2. `git submodule update --init --recursive` (if you want to use [PromptSafe](https://github.com/zinccat/PromptSafe) to secure your prompts from prompt leaking)
3. `conda env create -f environment.yml`
4. Add your own key to `scripts/key.py`
5. `streamlit run main.py`
6. Ta-dah!

For PromptSafe, also run `python initialize_promptsafe.py`
