array = [1,2,4,4,6,6,7];
var i = 0;
console.log("array.length = ", array.length);
for ( i = array.length; i >= 0 ; i--){
    console.log("i = ", i );
   console.log("array[i] = ", array[i]);   
   if ( array[i] % 2 == 0){
	array.splice(i,1);
    }
}

console.log("array = ", array);
