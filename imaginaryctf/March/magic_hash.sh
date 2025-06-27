generate_files() {
    index="$1"
    temp_dir=$(mktemp -d -t output)
    output1="$temp_dir/1-$index.out"
    output2="$temp_dir/2-$index.out"
    trap 'rm -f "$output1" "$output2"' EXIT
    echo "$output1 and $output2" >> log
    tmpfile=$(mktemp -t prefix)
    while true; do
        head -c 4096 < /dev/urandom > "$tmpfile"
        /Users/bluk/Developer/md5collgen/md5collgen -q "$tmpfile" -o "$output1" "$output2" 1>/dev/null
        python3 magic_hash.py "$output1" "$output2" >> log
    done
}

echo "" > log

for i in {1..7}; do
    generate_files "$i" &
done

wait