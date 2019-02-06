$('input:checkbox').change(
    function(){
        var column = $(this).attr("id")
        if ($(this).is(':checked')) {
          $('#foo tr > *:nth-child('+column+')').show();
        }
        else {
          $('#foo tr > *:nth-child('+column+')').hide();
        }
    });
