const getUser = require('../service/users.js');

module.exports = function accountRoute(req, res, next) {
    const userId = parseInt(req.query.userId, 10);
    if (userId >= 0) {
        getUser(userId)
            .then(user => res.render('account', { user }))
            .catch(next);
    } else {
        next(new Error(`Invalid userId received "${req.query.userId}"`));
    }
};
