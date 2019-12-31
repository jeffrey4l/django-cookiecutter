$(document).ready(function(){
    $('.volume-location1').click(function(evt){
        evt.preventDefault();
        $.ajax({
            url: '/',
            type: 'get',
            success: function(result){
                $('#result').html(result);
            },
        })
    });
})
