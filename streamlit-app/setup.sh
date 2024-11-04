mkdir -p ~/.streamlit/
#export PORT=8501
echo "\
[server]\n\
port = 8501\n\
enableCORS = true\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml