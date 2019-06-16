new Vue({
    el: '#app',
    data: () => ({
        mainHeaders: [
            { text: 'Registro', value: 'attendance_record' },
        ],
        attendance_records: [],
        incidences: [{date: "2019-05-12", window_state: false, incidence_type: 12}],
        incidence_types: [],
        record: "",
        type: 'month',
        start: '',
        end: '',
    }),
    methods: {
        getAttendanceRecordsAPI() {
            const path = 'http://127.0.0.1:8000/api/attendance-records/'
            axios.get(path).then((response) => {
                this.attendance_records = response.data;
            }).catch(function (error) {
                console.log(error);
            }).then(function () {
                // always executed
            });  
        },
        getIncidenceTypesAPI() {
            const path = 'http://127.0.0.1:8000/api/incidence-types/'
            axios.get(path).then((response) => {
                this.incidence_types = response.data;
            }).catch(function (error) {
                console.log(error);
            }).then(function () {
                // always executed
            });
        },
        getIncidencesAPI() {
            const path = 'http://127.0.0.1:8000/api/incidences/'
            axios.get(path).then((response) => {
                this.incidences = response.data;
                for (let index = 0; index < this.incidences.length; index++) {
                    const element = this.incidences[index];
                    const incidence_type = this.getIncidenceTypesInformation(element.incidence_type);
                    this.incidences[index] = {
                        'date': element.date,
                        'window_state': false,
                        'type': incidence_type.name,
                        'description': incidence_type.description,
                    };
                }
            }).catch(function (error) {
                console.log(error);
            }).then(function () {
                // always executed
            });
        },
        getIncidenceTypesInformation(id) {
            for (let index = 0; index < this.incidence_types.length; index++) {
                const element = this.incidence_types[index];
                if (element.id === id) {
                    return element;
                }
            }
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
        this.getAttendanceRecordsAPI();
        this.getIncidenceTypesAPI();
        this.getIncidencesAPI();
    },

});