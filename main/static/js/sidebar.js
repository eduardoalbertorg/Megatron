new Vue({
    el: '#app',
    data: () => ({
        mainHeaders: [
            { text: 'Registro', value: 'attendance_record' },
        ],
        attendance_records: [],
        record: "",
        type: 'month',
        start: '',
        end: '',
    }),
    methods: {
        getAttendanceRecords() {
            const path = 'http://localhost:8000/api/attendance-records/?format=json'
            axios.get(path).then((response) => {
                this.attendance_records = response.data;
              })
              .catch(function (error) {
                console.log(error);
              })
              .then(function () {
                // always executed
              });  
        }
    },
    created() {
        this.getAttendanceRecords();
    },

});