const Utils = {
    calculateNumber: (type, a, b) => {
        const roundedA = Math.round(a);
        const roundedB = Math.round(b);

        if (type === 'SUM') {
            return roundedA + roundedB;
        } else if (type === 'SUBTRACT') {
            return roundedA - roundedB;
        } else if (type === 'DIVIDE') {
            return roundedB === 0 ? 'Error' : roundedA / roundedB;
        }
    }
};

module.exports = Utils;
