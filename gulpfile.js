'use strict';

var gulp = require('gulp'),
    sass = require('gulp-sass'),
    runSequence = require('run-sequence'),
    browserSync = require('browser-sync'),
    exec = require('child_process').exec,
    reload = browserSync.reload;

gulp.task('styles', function() {
  gulp.src('web/assets/style.scss')
      .pipe(sass().on('error', sass.logError))
      .pipe(gulp.dest('web/static/'))
      .pipe(reload({ stream: true }));
});

gulp.task('build', ['styles']);

gulp.task('runServer', function() {
  exec('fab develop', function(err, stdout, stderr) {
    console.log(stdout);
    console.log(stderr);
  });
});

gulp.task('browserSync', ['build'], function() {
  browserSync.init([
    'web/**/*.css',
    'web/**/*.html'
  ], {
    proxy: '127.0.0.1:5000'
  });
});

gulp.task('watch', function() {
  gulp.watch('web/**/*.scss', ['styles']).on('change', reload);
  gulp.watch('web/**/*.html').on('change', reload);
});

gulp.task('develop', function() {
  runSequence('build', 'runServer', 'browserSync', 'watch')
});

gulp.task('default', ['build']);
