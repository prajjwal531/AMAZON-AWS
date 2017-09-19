application:
  name: UserDataService
  version: 2.7
  cluster: "${cluster}"
  virtualhost: "${virtualhost}"
  classloaderMode: ''
  resource_env_providers:
    res_env_provider1:
      name: UserDataResourceProvider
      factoryClassname: org.kp.wpp.is.property.util.PropertyManagerFactory
      classname: org.kp.wpp.is.property.util.PropertyManager
      res_env_entries1:
        name: UserDataServiceEnvEntries
        jndiName: env/UserDataServiceEnvEntries
        REEProperty1:
          name: PoolEvictionTime
          type: java.lang.Integer
          value: "${PoolEvictionTime}"
        REEProperty2:
          name: SwapDatabaseForNorthernColoradoServiceArea
          type: java.lang.Boolean
          value: "${SwapDatabaseForNorthernColoradoServiceArea}"
        REEProperty3:
          name: UDSStrategyConfig
          type: java.lang.String
          value: "${UDSStrategyConfig}"
        REEProperty4:
          name: MemberServiceEndPoint
          type: java.lang.String
          value: "${MemberServiceEndPoint}"
        REEProperty5:
          name: MWSTestMode
          type: java.lang.Boolean
          value: "${MWSTestMode}"
        REEProperty6:
          name: DataRefreshWindow
          type: java.lang.Integer
          value: "${DataRefreshWindow}"
        REEProperty7:
          name: MyChartServiceEndPoint
          type: java.lang.String
          value: "${MyChartServiceEndPoint}"
        REEProperty8:
          name: LdapURL
          type: java.lang.String
          value: "${LdapURL}"
        REEProperty9:
          name: LdapUserName
          type: java.lang.String
          value: "${LdapUserName}"
        REEProperty10:
          name: LdapPassword
          type: java.lang.String
          value: "${LdapPassword}"
        REEProperty11:
          name: RefreshWindowOverrideMax
          type: java.lang.Integer
          value: "${RefreshWindowOverrideMax}"
        REEProperty12:
          name: PoolMaxActive
          type: java.lang.Integer
          value: "${PoolMaxActive}"
        REEProperty13:
          name: BaseVersion
          type: java.lang.String
          value: "${BaseVersion}"
        REEProperty14:
          name: UDSActivateEpicAccount
          type: java.lang.Boolean
          value: "${UDSActivateEpicAccount}"
        REEProperty15:
          name: DMCMapExpirationMins
          type: java.lang.String
          value: "${DMCMapExpirationMins}"
        REEProperty16:
          name: RegionEnabledConfigString
          type: java.lang.String
          value: "${RegionEnabledConfigString}"
        REEProperty17:
          name: ValidAddressFieldsPatternMatchMapConfigString
          type: java.lang.String
          value: "${ValidAddressFieldsPatternMatchMapConfigString}"
        REEProperty18:
          name: ValidAddressStatesListConfigString
          type: java.lang.String
          value: "${ValidAddressStatesListConfigString}"
        REEProperty19:
          name: ValidAddressFieldsMinMaxlengthMapConfigString
          type: java.lang.String
          value: "${ValidAddressFieldsMinMaxlengthMapConfigString}"
        REEProperty20:
          name: TermsAndConditionsRoleConfigString
          type: java.lang.String
          value: "${TermsAndConditionsRoleConfigString}"
        REEProperty21:
          name: ConfigServiceBasicAuth
          type: java.lang.String
          value: "${ConfigServiceBasicAuth}"
        REEProperty22:
          name: ConfigServiceEnvironmentNode
          type: java.lang.String
          value: "${ConfigServiceEnvironmentNode}"
        REEProperty23:
          name: ConfigServiceMetaDataNode
          type: java.lang.String
          value: "${ConfigServiceMetaDataNode}"
        REEProperty24:
          name: ConfigServiceUrl
          type: java.lang.String
          value: "${ConfigServiceUrl}"
        REEProperty25:
          name: DataCenterLabel
          type: java.lang.String
          value: "${DataCenterLabel}"
        REEProperty26:
          name: EnvironmentLabel
          type: java.lang.String
          value: "${EnvironmentLabel}"
        REEProperty27:
          name: ConnectionTimeoutInMilliseconds
          type: java.lang.Integer
          value: "${ConnectionTimeoutInMilliseconds}"
        REEProperty28:
          name: RequestVolumeThreshold
          type: java.lang.Integer
          value: "${RequestVolumeThreshold}"
        REEProperty29:
          name: ErrorThresholdPercentage
          type: java.lang.Integer
          value: "${ErrorThresholdPercentage}"
        REEProperty30:
          name: SleepWindowInMilliseconds
          type: java.lang.Integer
          value: "${SleepWindowInMilliseconds}"
        REEProperty31:
          name: RollingPercentileWindowInMilliseconds
          type: java.lang.Integer
          value: "${RollingPercentileWindowInMilliseconds}"
        REEProperty32:
          name: RollingPercentileWindowBuckets
          type: java.lang.Integer
          value: "${RollingPercentileWindowInMilliseconds}"
        REEProperty33:
          name: ConfigServiceAccessToken
          type: java.lang.String
          value: "${ConfigServiceAccessToken}"
        REEProperty34:
          name: AsyncCorePoolSize
          type: java.lang.Integer
          value: "${AsyncCorePoolSize}"
        REEProperty35:
          name: AsyncMaxPoolSize
          type: java.lang.Integer
          value: "${AsyncMaxPoolSize}"
        REEProperty36:
          name: AsyncQueueCapacity
          type: java.lang.Integer
          value: "${AsyncQueueCapacity}"
        REEProperty37:
            name: CacheSyncMaxRetry
            type: java.lang.String
            value: "${CacheSyncMaxRetry}"
        REEProperty38:
            name: CacheSyncExecutorCorePoolSize
            type: java.lang.Integer
            value: "${CacheSyncExecutorCorePoolSize}"
        REEProperty39:
            name: CacheSyncExecutorMaxPoolSize
            type: java.lang.Integer
            value: "${CacheSyncExecutorMaxPoolSize}"
        REEProperty40:
            name: CacheSyncExecutorQueueCapacity
            type: java.lang.Integer
            value: "${CacheSyncExecutorQueueCapacity}"
        REEProperty41:
            name: CacheSyncConfigRefreshPeriod
            type: java.lang.Integer
            value: "${CacheSyncConfigRefreshPeriod}"
        REEProperty42:
            name: ConfigRefreshSchedulerPoolSize
            type: java.lang.Integer
            value: "${ConfigRefreshSchedulerPoolSize}"
        REEProperty43:
              name: MISEndPoint
              type: java.lang.String
              value: "${MISEndPoint}"
        REEProperty44:
              name: MISEnvValue
              type: java.lang.String
              value: "${MISEnvValue}"
        REEProperty45:
              name: MISPassword
              type: java.lang.String
              value: "${MISPassword}"
        REEProperty46:
              name: MISUsername
              type: java.lang.String
              value: "${MISUsername}"
        REEProperty47:
              name: MISTimeout
              type: java.lang.Integer
              value: "${MISTimeout}"
        REEProperty48:
              name: MISEnabled
              type: java.lang.Boolean
              value: "${MISEnabled}"
  jdbc_data_sources:
        data_source1:
              name: UserDataDS
              jndiName: jdbc/UserDataDS
              description: Support UDS svc ds
              providerType: Oracle JDBC Driver
              authDataAlias: WPCOAPP
              userId: "${wpp-user}"
              password: "${wpp-password}"
              dataStoreHelperClassName: com.ibm.websphere.rsadapter.Oracle11gDataStoreHelper
              resourceProperties:
                  DSProperty1:
                    name: URL
                    value: "${wpp-db}"
                    type: java.lang.String
                    description: This is the JDBC URL which connects to DB for a given environment.
              ConnectionPoolProperties:
                connectionTimeout: "${connectionTimeout}"
                maxConnections: "${maxConnections}"
                minConnections: "${minConnections}"
                reapTime: "${reapTime}"
                unusedTimeout: "${unusedTimeout}"
                agedTimeout: "${agedTimeout}"
                purgePolicy: "${purgePolicy}"
