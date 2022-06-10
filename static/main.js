let status_update_alert = $('#status_update')
let status_update_message = $('#status_update_message')

$( document ).ready(function() {
    status_update_alert.hide()

    $('#status').dataTable({
        searching: false, paging: false, info: false,
        "aoColumns": [
            { "mDataProp": "id" },
            { "mDataProp": "status",  render: function (data, type) {
                    var number = $.fn.dataTable.render
                        .number(',', '.', 2, '$')
                        .display(data);

                    if (type === 'display') {
                        let color = 'green';
                        if (data === 'fail') {
                            color = 'red';
                        } else if (data === 'warn') {
                            color = 'orange';
                        }
                        return '<span style="color:' + color + '">' + number + '</span>';
                    }
                    return number;
                },},
        ]
    });

    var detail_table = $('#detail_table').DataTable({
        lengthMenu: [15, 37],
        ajax: '/employees-ajax/',
        columns: [
            {
                className: 'dt-control',
                orderable: false,
                data: null,
                defaultContent: '',
            },
            { data: 'id' },
            { data: 'status' },
            { data: 'name' },
            { data: 'position' },
            { data: 'salary' },
            { data: 'last_updated' },
        ],
        }
        );
    $('#detail_table tbody').on('click', 'td.dt-control', function () {
            let tr = $(this).closest('tr');
            let row = detail_table.row(tr);

            if (row.child.isShown()) {
                // This row is already open - close it
                row.child.hide();
                tr.removeClass('shown');
            } else {
                // Open this row
                row.child(format_detail(row)).show();
                tr.addClass('shown');
            }
        });

    // EVENT TRIGGERS START
    $(document).on('click',".delete_record ",function(){
    let employee_id = this.value
    let items_to_post = {}
    let row_index = this.getAttribute("data-row");
    post_change(employee_id, items_to_post, "delete-employee")
      .then((data) => {
        console.log(data)
        if(data.error === false){
            //update the cell to reflect the change
            show_success_alert(data.message)
        }
      })
      .catch((error) => {
        console.log(error)
      })
    detail_table.row(row_index).remove().draw();
    });

    $(document).on('click',".clone_record ",function(){
    let employee_id = this.value
    let items_to_post = {}
    post_change(employee_id, items_to_post, "clone-employee")
      .then((data) => {
        console.log(data)
        if(data.error === false){
            //update the cell to reflect the change
            detail_table.row.add(
                { 'id': data.clone_employee_id,
                  'status': data.clone_status,
                  'name':  data.clone_name,
                  'position':  data.clone_position,
                  'salary':  data.clone_salary,
                  'last_updated':  data.clone_last_updated}).draw();
            show_success_alert(data.message)
            }

      })
      .catch((error) => {
        console.log(error)
      })
    });

  //Change status
  $(document).on('change',".change_status",function(){
      let employee_id = this.id.replace("status_", "")
      let row_index = this.getAttribute("data-row");
      detail_table.cell(row_index, 2).data(this.value).draw();
      let items_to_post = {"status":this.value}
      post_change(employee_id, items_to_post, "change-status")
      .then((data) => {
        console.log(data)
        if(data.error === false){
            //update the cell to reflect the change
            show_success_alert(data.message)
        }
      })
      .catch((error) => {
        console.log(error)
      })
    });

  //Change name
  $(document).on('change',".change_name",function(){
      let employee_id = this.id.replace("name_", "")
      let row_index = this.getAttribute("data-row");
      let items_to_post = {"name":this.value}
      post_change(employee_id, items_to_post, "change-name")
      .then((data) => {
        console.log(data)
        if(data.error === false){
            //update the cell to reflect the change
            detail_table.cell(row_index, 3).data(this.value).draw();
            show_success_alert(data.message)
        }
        else{
            status_update_alert.show()
            status_update_message.text(data.message)
            status_update_alert.removeClass('btn-success').addClass('alert-danger')
        }
      })
      .catch((error) => {
        console.log(error)
      })
    });

  //Change position
  $(document).on('change',".change_position",function(){
      let employee_id = this.id.replace("position_", "")
      let row_index = this.getAttribute("data-row");
      detail_table.cell(row_index, 4).data(this.value).draw();
      let items_to_post = {"position":this.value}
      post_change(employee_id, items_to_post, "change-position")
      .then((data) => {
        console.log(data)
        if(data.error === false){
            //update the cell to reflect the change
            show_success_alert(data.message)
        }
      })
      .catch((error) => {
        console.log(error)
      })
    });

    //Change salary
  $(document).on('change',".change_salary",function(){
      let employee_id = this.id.replace("salary_", "")
      let row_index = this.getAttribute("data-row");
      detail_table.cell(row_index, 5).data(this.value).draw();
      let items_to_post = {"salary":this.value}
      post_change(employee_id, items_to_post, "change-salary")
      .then((data) => {
        console.log(data)
        if(data.error === false){
            //update the cell to reflect the change
            show_success_alert(data.message)
        }
      })
      .catch((error) => {
        console.log(error)
      })
    });
  // END JQUERY
  });


function format_detail(row) {
    let d = row.data()
    // `d` is the original data object for the row
    return (
        '<table>' +
        '<tr>' +
          '<td>' + draw_status_select(d.status, d.id, row.index()) + '</td>' +
          '<td>' + draw_text_input('change_name', d.id, d.name, row.index()) + '</td>' +
          '<td>' + draw_text_input('change_position', d.id, d.position, row.index()) + '</td>' +
          '<td>' + draw_text_input('change_salary', d.id, d.salary, row.index()) + '</td>' +
          '<td><button class="delete_record" value="' + d.id  +'" " data-row="' + row.index() + '">Delete</button> </td>' +
          '<td><button class="clone_record"  value="' + d.id  +'">Clone</button> </td>' +
        '</tr>' +
        '</table>'
    );
}

function show_success_alert(message){
    status_update_alert.show()
    status_update_alert.removeClass('alert-danger').addClass('btn-success')
    status_update_message.text(message)

}


function draw_text_input(class_name, id, value, row){
   return '<input type="text" class="' + class_name + '" id="' + id  +'" value="' + value + '" data-row="' + row + '">'
}

function draw_status_select(status, id, row_index){
  const statuses = ['warn', 'fail', 'pass']
  let select_box = '<select class="change_status" data-row="' + row_index + '" id="status_' + id + '">'

  for (let i = 0; i < statuses.length; i++) {
    select_box += '<option value="' + statuses[i] + '" ' + selected(status, statuses[i]) + '>' + statuses[i] + '</option>'
  }
  select_box += '</select>'
  return select_box
}
function selected(status, selected_status){
  if (status === selected_status){
    return "selected"
  }
  else{
    return ""
  }

}

