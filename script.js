// global variables
var name = 'vignesh'
var age = '12'

function add() {
    // local variables
    var a =33;
    var b =10;
    var c =a/b;
    document.write(c);
}   
function show() {
    
    document.write('Hello Javascript');
}


function aa(){
    alert('Hello you are good at learning new skills Man!!')
}


// to calla globalelement inside a function u use window object as below
function cond_stmts(){  
    if (window.age == "21"){
        document.write('age is twenty');
    }
    else if(window.age == "20"){
        document.write('age is twenty one');
    
    }

    else{
        document.write("age is not relevant");
    
    }
}