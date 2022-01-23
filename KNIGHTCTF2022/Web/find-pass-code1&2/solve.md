# Passcode 1

> Note a difference between 5.2 and 5.3 versions

>echo (int)strcmp('pending',array());
will output -1 in PHP 5.2.16 (probably in all versions prior 5.3)
but will output 0 in PHP 5.3.3

> Of course, you never need to use array as a parameter in string comparisons.


That is, we just use `passcode[]=a` to get around `strcmp($passcode,$flag) == 0` 

# Passcode 2

They are using `==` to compare a md5-hash, which is base 16 in PHP against the passcode. The comparison will do some type-juggling which is dangerous if the strings are numbers. Therefore `0e111 == 0e222` because in floating point settings, both numbers are `0`. Hence we have to find an input such that `$passcode == md5($passcode)`. There are some, but we have to look for new ones, because existing ones are checked.