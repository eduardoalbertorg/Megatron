new Vue({
    el: '#app',
    data: () => ({
        mainHeaders: [
            { text: 'Registro', value: 'attendance_record' },
        ],
        attendance_records: [],
        incidences: [{date: "2019-05-12", window_state: false, incidence_type: 12}],
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
        },
        getIncidences() {
            const path = 'http://127.0.0.1:8000/api/incidences/'
            axios.get(path).then((response) => {
                this.incidences = response.data;
                for (let index = 0; index < this.incidences.length; index++) {
                    const element = this.incidences[index];
                    this.incidences[index] = {
                        'date': element.date,
                        'window_state': false,
                        'incidence_type': element.incidence_type,
                    };
                }
                console.log(this.incidences);
            }).catch(function (error) {
                console.log(error);
            }).then(function () {
                // always executed
            });
        },
    },
    computed: {
        incidencesMap() {
            const map = {};
            this.incidences.forEach(e => (map[e.date] = map[e.date] || []).push(e));
            return map;
        }
    },
    created() {
        this.getAttendanceRecords();
        this.getIncidences();
    },

});