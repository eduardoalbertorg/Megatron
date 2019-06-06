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
            const path = 'http://127.0.0.1:8000/api/attendance-records/'
            axios.get(path).then((response) => {
                this.attendance_records = response.data;
            }).catch(function (error) {
                console.log(error);
            }).then(function () {
                // always executed
            });  
        }
    },
    created() {
        this.getAttendanceRecords();
    },

});