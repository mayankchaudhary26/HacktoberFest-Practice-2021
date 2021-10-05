if (process.env.NODE_ENV === 'production') {
	module.exports = {
		PORT: process.env.PORT,
	};
} else {
	module.exports = {
		...require('./dev.config'),
	};
}
