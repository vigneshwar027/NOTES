$(document).ready(function(){

    
    $('input:checkbox').prop('checked',false);

    $('a[id=email]').css("color","red");

    $(document).click(function(){

       
            $('#quest').toggle()
       
    });

   
});


$('#data').data({"name":'vignesh',"age":45});

$('button').filter('#action').click(function(){
    $('#last').data({"action":"data is passed"});

    var dat = $('#last').data()
    console.log(typeof dat["action"]);

    })    

    // console.log($('#data').data())
    // $('#last').text($('#first').text())

;

        