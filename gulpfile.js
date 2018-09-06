var gulp = require('gulp'),
    sass = require('gulp-sass'),
    runSequence = require('run-sequence'),
    browserSync = require('browser-sync'),
    rename = require('gulp-rename'),
    babel = require('gulp-babel'),
    sourcemaps = require('gulp-sourcemaps'),
    exec = require('child_process').exec,
    reload = browserSync.reload;

gulp.task('styles', function() {
  gulp.src('web/assets/styles/index.scss')
      .pipe(sourcemaps.init())
      .pipe(sass().on('error', sass.logError))
      .pipe(sourcemaps.write())
      .pipe(rename('style.css'))
      .pipe(gulp.dest('web/static/'))
      .pipe(reload({ stream: true }));
});

gulp.task('scripts', function() {
  gulp.src('web/assets/scripts/index.js')
      .pipe(sourcemaps.init())
      .pipe(babel({
        presets: ['env'],
        plugins: ['add-module-exports']
      }))
      .pipe(sourcemaps.write())
      .pipe(rename('script.js'))
      .pipe(gulp.dest('web/static/'))
      .pipe(reload({ stream: true }));
});

gulp.task('build', ['styles', 'scripts']);

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
  gulp.watch('web/assets/styles/*.scss', ['styles']).on('change', reload);
  gulp.watch('web/assets/scripts/*.js', ['scripts']).on('change', reload);
  gulp.watch('web/**/*.html').on('change', reload);
});

gulp.task('run', function() {
  runSequence('build', 'runServer', 'browserSync', 'watch')
});

gulp.task('default', ['build']);
