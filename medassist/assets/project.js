$(document).ready(function(){
    $.getJSON('/specializationdisplayJSON',function(data){
    
        data.result.map((item)=>{
        $('#spld').append($('<option>').text(item.specialization).val(item.specializationid))
        $('#specialization').append($('<option>').text(item.specialization).val(item.specializationid))
    
        }) 
    $('#specialization').change(function(){
        $('#subque').empty()
        $('#subque').append($('<option disable selected>').text('-Question-'))
            
              
    $.getJSON('/subquestiondisplayJSON',{'specializationid':$('#specialization').val()},function(data){
        data.result.map((item)=>{
        $('#subque').append($('<option>').text(item.question).val(item.questionid))
                         
    })    
})
    })
})
})
