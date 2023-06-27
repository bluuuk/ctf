vm:
	docker run -it -v $$(pwd)/:/mnt/host -w /mnt/host rust:1.67-slim-buster cargo build --release
	cp target/release/vm vm
