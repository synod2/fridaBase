
var baseAddr = Module.findBaseAddress('notepad.exe');
var func_addr = resolveAddress(0xDEADBEEF);

// Interceptor.attach(func_addr,{
//     onEnter : function(args){

//     },
//     onleave : function(retval){

//     }
// })


//console.log("initialize Sleep\n");
//Thread.sleep(10);

function resolveAddress(addr){
    //var idaBase = ptr('0x400000');
    var idaBase = ptr('0x0');
    var offset = ptr(addr).sub(idaBase);
    var result = baseAddr.add(offset);
    console.log('[+] NewAddr =' + result);
    return result 
}