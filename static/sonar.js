

      $(document).ready(function() {

        $("#loadingModal").modal({backdrop: 'static', keyboard: 'false'});

        // Load the Visualization API and the corechart package.
        google.charts.load('current', {'packages':['corechart', 'bar', 'line'], 'callback': initLoad});

        // Set a callback to run when the Google Visualization API is loaded.
           //google.charts.setOnLoadCallback(loadData);

          // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.


     function initLoad(){

        <!-- bootstrap-daterangepicker -->

        var cb = function(start, end, label) {
          console.log(start.toISOString(), end.toISOString(), label);
          $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
        };

        var optionSet1 = {
          startDate: moment().subtract(14, 'days'),
          endDate: moment(),
          minDate: '01/01/2000',
          maxDate: moment().format('MM/DD/YYYY'),
          dateLimit: {
            days: 3660
          },
          showDropdowns: true,
          showWeekNumbers: true,
          timePicker: false,
          timePickerIncrement: 1,
          timePicker12Hour: true,
          ranges: {
            '14 Days Interval': [moment().subtract(14, 'days'), moment()],
            '30 Days Interval': [moment().subtract(30, 'days'), moment()],
            '3 Months Interval': [moment().subtract(3, 'month'), moment()],
            '6 Months Interval': [moment().subtract(6, 'month'), moment()],
          },
          opens: 'left',
          buttonClasses: ['btn btn-default'],
          applyClass: 'btn-small btn-primary',
          cancelClass: 'btn-small',
          format: 'MM/DD/YYYY',
          separator: ' to ',
          locale: {
            applyLabel: 'Submit',
            cancelLabel: 'Clear',
            fromLabel: 'From',
            toLabel: 'To',
            customRangeLabel: 'Choose Period',
            daysOfWeek: ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'],
            monthNames: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            firstDay: 1
          }
        };
        loadData(optionSet1.startDate.format(), optionSet1.endDate.format());
        $('#reportrange span').html(moment().subtract(14, 'days').format('MMMM D, YYYY') + ' - ' + moment().format('MMMM D, YYYY'));
        $('#reportrange').daterangepicker(optionSet1, cb);
        $('#reportrange').on('show.daterangepicker', function() {
          console.log("show event fired");
        });
        $('#reportrange').on('hide.daterangepicker', function() {
          console.log("hide event fired");
        });
        $('#reportrange').on('apply.daterangepicker', function(ev, picker) {
          console.log("apply event fired, start/end dates are " + picker.startDate.format('MMMM D, YYYY') + " to " + picker.endDate.format('MMMM D, YYYY'));
          loadData(picker.startDate.format(), picker.endDate.format());
          $("#loadingModal").modal({backdrop: 'static', keyboard: 'false'});
        });
        $('#reportrange').on('cancel.daterangepicker', function(ev, picker) {
          console.log("cancel event fired");
        });
        $('#options1').click(function() {
          $('#reportrange').data('daterangepicker').setOptions(optionSet1, cb);
        });
        $('#options2').click(function() {
          $('#reportrange').data('daterangepicker').setOptions(optionSet2, cb);
        });
        $('#destroy').click(function() {
          $('#reportrange').data('daterangepicker').remove();
        });


    <!-- /bootstrap-daterangepicker -->

     }







});