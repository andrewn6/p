# Starts a dev server
cd packages/falafel

if [[ $1 == "-"*"d"* || $1 == "--dev"* ]]; then
    bun run dev
else  
    bun run preview
fi