var str1n9 = require('str1n9');

var generator = new Vue({
    el: '#generator',
    data: {
        output: '请点击召唤密码按钮',
        filter: {
            capital: true,
            letter: true,
            number: true,
            punctuation: false,
            length: 8
        },
        format: null
    },
    methods: {
        updateOutput: function () {
            var types = (this.$get('filter.capital') ? 'c' : '') +
                (this.$get('filter.letter') ? 'l' : '') +
                (this.$get('filter.number') ? 'n' : '') +
                (this.$get('filter.punctuation') ? 'p' : '');

            types = types || 'cpln';

            var length = this.$get('filter.length') || 8;

            this.$set('output', str1n9.randomString(length, types, this.$get('format')));
        }
    }
});

generator.$watch('filter', function (val) {
    this.updateOutput();
}, {deep: true});

generator.$watch('format', function (val) {
    if (!/^[clnp]+$/.test(val)) {
        if (val !== '') {
            alert('规则输入错误')
            return;
        }
    }
    this.updateOutput();
});
