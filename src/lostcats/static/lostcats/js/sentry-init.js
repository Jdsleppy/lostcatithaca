Sentry.init({
  dsn: "https://733ff8b4c88e49bcbc15d090e0a01250@o867951.ingest.sentry.io/5823946",
  // this assumes your build process sets "npm_package_version" in the env
  release: "lostcat@1.0.0",
  //   integrations: [new Sentry.Integrations.BrowserTracing()],

  // We recommend adjusting this value in production, or using tracesSampler
  // for finer control
  tracesSampleRate: 1.0,
});
