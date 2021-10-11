maxValue = 0;
maxIndex = 8;

for(var i = 0; i < 16; i++){
var average = (scanArray[i] + scanArray[i+1] + scanArray[i+2]);

 if(average > maxValue){
  maxIndex = i+1;
  maxValue=average;
 }
}

return maxIndex - 8;

/*

CTF{cbe138a2cd7bd97ab726ebd67e3b7126707f3e7f}

*/