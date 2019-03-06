$('input:checkbox').change(
  function() {
    var column = $(this).attr("id")
    if (column == "all") {
      for (var i = 0; i < 20; i++) {
        var defid = i.toString()
        $('#foo tr > *:nth-child(' + defid + ')').show();
        $('#' + defid).prop("checked", true);
      }
      $('#all').prop("checked", false);
    } else if (column == "default") {
      for (var i = 0; i < 20; i++) {
        var defid = i.toString()
        if (['1', '2', '3', '5', '6'].indexOf(defid) >= 0) {
          $('#foo tr > *:nth-child(' + defid + ')').show()
          $('#' + defid).prop("checked", true);
        } else {
          $('#foo tr > *:nth-child(' + defid + ')').hide();
          $('#' + defid).prop("checked", false);
        }
      }
      $('#default').prop("checked", false);
    } else if ($(this).is(':checked')) {
      $('#foo tr > *:nth-child(' + column + ')').show();
    } else {
      $('#foo tr > *:nth-child(' + column + ')').hide();
    }
  });
