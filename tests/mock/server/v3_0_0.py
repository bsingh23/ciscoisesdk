from http.server import BaseHTTPRequestHandler
import re
import json
import requests


class MockServerRequestHandler_v3_0_0(BaseHTTPRequestHandler):
    TASKS_38eb7df265a55d2cbedb08847549b39a_PATTERN = re.compile(r"/api/v1/task")
    TASKS_bcee1c9523a45056ab79dc64bdf827fe_PATTERN = re.compile(r"/api/v1/task/string")
    NODE_DEPLOYMENT_fa838e78175e51b4bcfb0821c19b81b7_PATTERN = re.compile(r"/api/v1/deployment/node/")
    NODE_DEPLOYMENT_e82e46732de25832a543c4640312588c_PATTERN = re.compile(r"/api/v1/deployment/node/")
    NODE_DEPLOYMENT_42b11e2f1af656bcb5880a7b33720ec5_PATTERN = re.compile(r"/api/v1/deployment/node-promotion/")
    NODE_DEPLOYMENT_ae8d7c8f33bb52ceb04880845f2f45ba_PATTERN = re.compile(r"/api/v1/deployment/node/string")
    NODE_DEPLOYMENT_682c1fa3bf115c77be99b602aca1493b_PATTERN = re.compile(r"/api/v1/deployment/node/string")
    NODE_DEPLOYMENT_161d26670a205a78800cb50673027a6e_PATTERN = re.compile(r"/api/v1/deployment/node/string")
    NODE_GROUP_a0824f9a589c58cd8df522524cb550ad_PATTERN = re.compile(r"/api/v1/deployment/node-group")
    NODE_GROUP_64a0aadd33595645bf671efc4912f89a_PATTERN = re.compile(r"/api/v1/deployment/node-group/string")
    NODE_GROUP_f41d844dbee15f7680920652004f69b6_PATTERN = re.compile(r"/api/v1/deployment/node-group/string")
    NODE_GROUP_2875a99695fd5ee0b00efce79a5761ff_PATTERN = re.compile(r"/api/v1/deployment/node-group/string")
    NODE_GROUP_2c5c37c343c050e0af67b2223e64faf3_PATTERN = re.compile(r"/api/v1/deployment/node-group/string")
    PAN_HA_02daa171ab765a02a714c48376b3790d_PATTERN = re.compile(r"/api/v1/deployment/pan-ha")
    PAN_HA_fc9a4ee495785518bd2251b6b4fb41f4_PATTERN = re.compile(r"/api/v1/deployment/pan-ha")
    PAN_HA_a1e3cde0c3f254b39caaaf7c907ae67e_PATTERN = re.compile(r"/api/v1/deployment/pan-ha")
    REPLICATION_STATUS_7ae615b5e28c54639f44bd10e5b36601_PATTERN = re.compile(r"/api/v1/replication-status/string")
    SYNC_ISE_NODE_582ad69fa1d850f4993bbfc888749fa0_PATTERN = re.compile(r"/api/v1/deployment/sync-node")
    BACKUP_AND_RESTORE_b9638a67f60d5a6aa476af13632d96bd_PATTERN = re.compile(r"/v1/backup-restore/config/backup")
    BACKUP_AND_RESTORE_39527e9813ff50a9bcbbd5d539ed19d8_PATTERN = re.compile(r"/v1/backup-restore/config/cancel-backup")
    BACKUP_AND_RESTORE_b0b71a5f25825202b6cb339ce1a5a8d4_PATTERN = re.compile(r"/v1/backup-restore/config/last-backup-status")
    BACKUP_AND_RESTORE_db3505847b4e5f37a5c74bc41df54be3_PATTERN = re.compile(r"/v1/backup-restore/config/restore")
    BACKUP_AND_RESTORE_5329d31fa60f5575a2ed23cee473c0fc_PATTERN = re.compile(r"/v1/backup-restore/config/schedule-config-backup")
    BACKUP_AND_RESTORE_dd4581dd32f65e8c83cca2f0a97af3e2_PATTERN = re.compile(r"/v1/backup-restore/config/schedule-config-backup")
    REPOSITORY_a83213678e6b58528986f1219d9f12ce_PATTERN = re.compile(r"/v1/repository")
    REPOSITORY_17edcb0e8c6b54709d4d61ea23b45f84_PATTERN = re.compile(r"/v1/repository")
    REPOSITORY_8a79dc5595ac51d1970b8d53498d3c32_PATTERN = re.compile(r"/v1/repository/string")
    REPOSITORY_62488ad8eb56595e86c4300607ec4dd3_PATTERN = re.compile(r"/v1/repository/string")
    REPOSITORY_d3b49f09d7f954bdb6f413e1785a05d7_PATTERN = re.compile(r"/v1/repository/string")
    REPOSITORY_fc645a4297f55557af8d398f07f6d0a0_PATTERN = re.compile(r"/v1/repository/string/files")
    ANC_ENDPOINT_5ffbc09a97795b8d872a943895c00345_PATTERN = re.compile(r"/ers/config/ancendpoint/string")
    ANC_ENDPOINT_2131fc6670fd50dfb04b1f6b16981256_PATTERN = re.compile(r"/ers/config/ancendpoint/clear")
    ANC_ENDPOINT_502e681462295b8b8faea9ce6099ff0c_PATTERN = re.compile(r"/ers/config/ancendpoint")
    ANC_ENDPOINT_136bc936bcb25464b9f3f227647b0443_PATTERN = re.compile(r"/ers/config/ancendpoint/apply")
    ANC_ENDPOINT_d5eb6cea45635ef58f5bc624de004f16_PATTERN = re.compile(r"/ers/config/ancendpoint/versioninfo")
    ANC_ENDPOINT_5e6167fc5cb6593b8b48429187a26a67_PATTERN = re.compile(r"/ers/config/ancendpoint/bulk/submit")
    ANC_ENDPOINT_0a1c6b9323e55505830673a1819840f3_PATTERN = re.compile(r"/ers/config/ancendpoint/bulk/string")
    ANC_POLICY_983a095b061f564ebba331f66505b0e3_PATTERN = re.compile(r"/ers/config/ancpolicy/name/string")
    ANC_POLICY_f41f77362663580d8cc3e6e88623889d_PATTERN = re.compile(r"/ers/config/ancpolicy/string")
    ANC_POLICY_1d79b507bda155c180d42f0a67ef64d5_PATTERN = re.compile(r"/ers/config/ancpolicy/string")
    ANC_POLICY_7c6b8dd764e052699d4d7a0d8ba43640_PATTERN = re.compile(r"/ers/config/ancpolicy/string")
    ANC_POLICY_440813c9722c56108cac8ca50bf8f01c_PATTERN = re.compile(r"/ers/config/ancpolicy")
    ANC_POLICY_2acfdb4060de5a1895b383238c205986_PATTERN = re.compile(r"/ers/config/ancpolicy")
    ANC_POLICY_b01a12e2b55e582084fab915465bf962_PATTERN = re.compile(r"/ers/config/ancpolicy/versioninfo")
    ANC_POLICY_4d67f9f6fba65dcbbcf64ca3e31b39a6_PATTERN = re.compile(r"/ers/config/ancpolicy/bulk/submit")
    ANC_POLICY_10023cdff02b5185b9b54c9e58762704_PATTERN = re.compile(r"/ers/config/ancpolicy/bulk/string")
    CLEAR_THREATS_AND_VULNERABILITIES_e3110fc63ecb5428a075a8af8497fb35_PATTERN = re.compile(r"/ers/config/threat/clearThreatsAndVulneribilities")
    CLEAR_THREATS_AND_VULNERABILITIES_83379c74d24e5ae9bb90f798a190cca3_PATTERN = re.compile(r"/ers/config/threat/versioninfo")
    NODE_DETAILS_ab48268c76aa598788a5ebc370226f3a_PATTERN = re.compile(r"/ers/config/node/name/string")
    NODE_DETAILS_0397bb2e9d6651c7bf18c1b60ff7eb14_PATTERN = re.compile(r"/ers/config/node/string")
    NODE_DETAILS_775d9b8599f55fc4a1bd9d6ac02619eb_PATTERN = re.compile(r"/ers/config/node")
    NODE_DETAILS_ca9a3d8217d5507aa11020bee82ef228_PATTERN = re.compile(r"/ers/config/node/versioninfo")
    PSN_NODE_DETAILS_WITH_RADIUS_SERVICE_ab225d0b2a6c52a99df1f1d8fb6a4dac_PATTERN = re.compile(r"/ers/config/sessionservicenode/name/string")
    PSN_NODE_DETAILS_WITH_RADIUS_SERVICE_c988bb742d055294b74b4d6916ca1ada_PATTERN = re.compile(r"/ers/config/sessionservicenode/string")
    PSN_NODE_DETAILS_WITH_RADIUS_SERVICE_66dccbf248575cbeb3cd3dda5cdbcf20_PATTERN = re.compile(r"/ers/config/sessionservicenode")
    PSN_NODE_DETAILS_WITH_RADIUS_SERVICE_05c0bfee23f95034842993a83d77c4e4_PATTERN = re.compile(r"/ers/config/sessionservicenode/versioninfo")
    PULL_DEPLOYMENT_INFO_f9159c9f9a1951568daee7080e1dda47_PATTERN = re.compile(r"/ers/config/deploymentinfo/getAllInfo")
    PULL_DEPLOYMENT_INFO_8698cc09209259dcbde7c851b5a6eda6_PATTERN = re.compile(r"/ers/config/deploymentinfo/versioninfo")
    PX_GRID_NODE_a2a7f23f85105113954c87a917b7455f_PATTERN = re.compile(r"/ers/config/ers/config/pxgridNode/name/string/approve")
    PX_GRID_NODE_111a9d109aac585a89bdd3fae400064b_PATTERN = re.compile(r"/ers/config/pxgridNode/name/string")
    PX_GRID_NODE_849e718d5054593b94a2fef39461c24a_PATTERN = re.compile(r"/ers/config/pxgridNode/name/string")
    PX_GRID_NODE_d24ade0b53405fbc898cb0cc1ea57fb8_PATTERN = re.compile(r"/ers/config/pxgridNode/string")
    PX_GRID_NODE_52661028d97156379640002f79b2007c_PATTERN = re.compile(r"/ers/config/pxgridNode")
    PX_GRID_NODE_73c2962d70ef5964be55cfeae68e5ba6_PATTERN = re.compile(r"/ers/config/pxgridNode/versioninfo")
    SUPPORT_BUNDLE_DOWNLOAD_737531846d125b968b9d362a3458621d_PATTERN = re.compile(r"/ers/config/supportbundledownload")
    SUPPORT_BUNDLE_DOWNLOAD_25c57752629f546fb86e84c59285350f_PATTERN = re.compile(r"/ers/config/supportbundledownload/versioninfo")
    SUPPORT_BUNDLE_STATUS_cec7dc317e875ff0a315a7c0556f9c51_PATTERN = re.compile(r"/ers/config/supportbundlestatus/string")
    SUPPORT_BUNDLE_STATUS_505300e162f051d58c6ae9d5e3851780_PATTERN = re.compile(r"/ers/config/supportbundlestatus")
    SUPPORT_BUNDLE_STATUS_7ae30c71acc45385a6b3e9a49a8281a9_PATTERN = re.compile(r"/ers/config/supportbundlestatus/versioninfo")
    SUPPORT_BUNDLE_TRIGGER_CONFIGURATION_492171fac48e5c63abfe2feec6fd1903_PATTERN = re.compile(r"/ers/config/supportbundle")
    SUPPORT_BUNDLE_TRIGGER_CONFIGURATION_a2b17c3c4eab52caa2fc7c811965c79d_PATTERN = re.compile(r"/ers/config/supportbundle/versioninfo")
    CERTIFICATES_87efa004c89a5b85ad30e0dde622bfaf_PATTERN = re.compile(r"/v1/certs/certificate-signing-request")
    CERTIFICATES_dd7a13ef2dea5b9fa6c4d67839133bbf_PATTERN = re.compile(r"/v1/certs/certificate-signing-request")
    CERTIFICATES_0910f99dc34755cf954945d5575e3072_PATTERN = re.compile(r"/v1/certs/certificate-signing-request/export/string/string")
    CERTIFICATES_db47e53374a85830af220e5f982d10da_PATTERN = re.compile(r"/v1/certs/certificate-signing-request/intermediate-ca")
    CERTIFICATES_5015d080d7635e27aef80f42d20b01c8_PATTERN = re.compile(r"/v1/certs/certificate-signing-request/string/string")
    CERTIFICATES_dde06bf20b6b5f71b8f0782f3750c242_PATTERN = re.compile(r"/v1/certs/certificate-signing-request/string/string")
    CERTIFICATES_7222975970e85c38bcad4249948c550b_PATTERN = re.compile(r"/v1/certs/ise-root-ca/regenerate")
    CERTIFICATES_ce788c3408de5056a2e71955f86d6f05_PATTERN = re.compile(r"/v1/certs/renew-certificate")
    CERTIFICATES_77c39f0f97cb53e19a03f2ea53f5b831_PATTERN = re.compile(r"/v1/certs/signed-certificate/bind")
    CERTIFICATES_da5ac537bf475538b7bc42c8cce2e530_PATTERN = re.compile(r"/v1/certs/system-certificate/export")
    CERTIFICATES_adde5bf7c9185218b955ff0c365fcc4c_PATTERN = re.compile(r"/v1/certs/system-certificate/import")
    CERTIFICATES_c2e43687a3205903a3f60728b87f1865_PATTERN = re.compile(r"/v1/certs/system-certificate/string")
    CERTIFICATES_c4e07bc79feb5e19bf6cc60220f47bdf_PATTERN = re.compile(r"/v1/certs/system-certificate/string/string")
    CERTIFICATES_e9594a91bd735eaabe2eb50038e9d05a_PATTERN = re.compile(r"/v1/certs/system-certificate/string/string")
    CERTIFICATES_5c55df3640a55c48bece27159ce199f8_PATTERN = re.compile(r"/v1/certs/system-certificate/string/string")
    CERTIFICATES_df7d8ed3e15a5d1587cdd7652efe0104_PATTERN = re.compile(r"/v1/certs/trusted-certificate")
    CERTIFICATES_5978827945b45792ab0b40c8a2d3392c_PATTERN = re.compile(r"/v1/certs/trusted-certificate/export/string")
    CERTIFICATES_f385b6330ef6500cb599f55407695a3e_PATTERN = re.compile(r"/v1/certs/trusted-certificate/import")
    CERTIFICATES_bee89e08a5145417989aaf187a6d7b2b_PATTERN = re.compile(r"/v1/certs/trusted-certificate/string")
    CERTIFICATES_ed4e0ba952525984acfe4a151689c2eb_PATTERN = re.compile(r"/v1/certs/trusted-certificate/string")
    CERTIFICATES_de9ebc73cfce5059a702076cf6a0aec2_PATTERN = re.compile(r"/v1/certs/trusted-certificate/string")
    DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_e8bd869250105a2ba30dd2cb65b0b3f2_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/authentication")
    DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_73164e92c5af5344b4d9fdc45a282ce5_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/authentication")
    DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_573a1a3596305814bab0a6d05cf86280_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/authentication/reset-hitcount")
    DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_87d71c8af3b55abb8e5959965baf2043_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/authentication/string")
    DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_7dc678d472905ab5bce9f4cba7cd7004_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/authentication/string")
    DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_a0a005e87c6755e0bf5d4454a98f08c5_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/authentication/string")
    DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_0eb446266e3d54f4a657050d4f9b0bf9_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/exception")
    DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_c730e85640aa5a59bc0e0fd95dacf889_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/exception")
    DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_2dde23cf27e65a60a949d8f1f599b3d2_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/exception/reset-hitcount")
    DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_5afaa335e2545c6f8f5530cd5686366a_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/exception/string")
    DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_e326f7a61069587f9a27e69433229cc7_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/exception/string")
    DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_7c12c4eb2a5650c2b6e26a84131ef65b_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/exception/string")
    DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_d407475db88f596390eab0a3e8c1d162_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/global-exception")
    DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_8558ade26d445251a45cc753f68d21bc_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/global-exception")
    DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_6b273ca0ffac58c3921f658152c03dbb_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/global-exception/reset-hitcount")
    DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_3a3d7e48a50d58a8a5d5720f9d55cf45_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/global-exception/string")
    DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_28042265da96552991705623287a164c_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/global-exception/string")
    DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_10281a20040d51a1ba61f4d210195e59_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/global-exception/string")
    DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_4e4ac2543c3b53b5982168169f0b29b4_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/authorization")
    DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_8440a5fd2b5d5306b9941387f400c7a0_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/authorization")
    DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_38edb17577d9503ba1155c2916dcf663_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/authorization/reset-hitcount")
    DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_f1d11ab85a0a5597b9513d92a894ef1b_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/authorization/string")
    DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_80b60ed1eed75d7d9091344f4e38e2f1_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/authorization/string")
    DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_e7979abd11155f12b1336bbf02a99687_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string/authorization/string")
    DEVICE_ADMINISTRATION_COMMAND_SET_273e0977618453b1b00e1c2b4cfa1999_PATTERN = re.compile(r"/v1/policy/device-admin/command-sets")
    DEVICE_ADMINISTRATION_CONDITIONS_fdfa9b301f925a34a848f29f223e5b8d_PATTERN = re.compile(r"/v1/policy/device-admin/condition")
    DEVICE_ADMINISTRATION_CONDITIONS_b84dbd77c49f5056b9bf3c1e496ebe5f_PATTERN = re.compile(r"/v1/policy/device-admin/condition")
    DEVICE_ADMINISTRATION_CONDITIONS_316863dcb2ca563999b2d3691e1def79_PATTERN = re.compile(r"/v1/policy/device-admin/condition/authentication")
    DEVICE_ADMINISTRATION_CONDITIONS_e67076b912ef5362949be22842642596_PATTERN = re.compile(r"/v1/policy/device-admin/condition/authorization")
    DEVICE_ADMINISTRATION_CONDITIONS_3d9fe67eb28858609eca3907c8343015_PATTERN = re.compile(r"/v1/policy/device-admin/condition/condition-by-name/string")
    DEVICE_ADMINISTRATION_CONDITIONS_f0540adc16725e00adffdf57b67fb6ba_PATTERN = re.compile(r"/v1/policy/device-admin/condition/condition-by-name/string")
    DEVICE_ADMINISTRATION_CONDITIONS_c276cf1dc9545d45ae3f871966cb664b_PATTERN = re.compile(r"/v1/policy/device-admin/condition/condition-by-name/string")
    DEVICE_ADMINISTRATION_CONDITIONS_68b404b307a35c2d9438da695bb49c54_PATTERN = re.compile(r"/v1/policy/device-admin/condition/policyset")
    DEVICE_ADMINISTRATION_CONDITIONS_27c0cf6ab73353ffa2b6986a9b16c54e_PATTERN = re.compile(r"/v1/policy/device-admin/condition/string")
    DEVICE_ADMINISTRATION_CONDITIONS_3b9b1bfd0f4151eb9812b474e4e4fa3c_PATTERN = re.compile(r"/v1/policy/device-admin/condition/string")
    DEVICE_ADMINISTRATION_CONDITIONS_2a6c1759c65b51a09ed7981397ece5c6_PATTERN = re.compile(r"/v1/policy/device-admin/condition/string")
    DEVICE_ADMINISTRATION_DICTIONARY_ATTRIBUTES_LIST_7f1ff6e8bb2d5c7fbcf39fbadf5da2d5_PATTERN = re.compile(r"/v1/policy/device-admin/dictionaries/authentication")
    DEVICE_ADMINISTRATION_DICTIONARY_ATTRIBUTES_LIST_6e2f955f29ce511993a189f2d234048d_PATTERN = re.compile(r"/v1/policy/device-admin/dictionaries/authorization")
    DEVICE_ADMINISTRATION_DICTIONARY_ATTRIBUTES_LIST_892e064032895c8098927d3a39ef6af2_PATTERN = re.compile(r"/v1/policy/device-admin/dictionaries/policyset")
    DEVICE_ADMINISTRATION_IDENTITY_STORES_7ae7d98a7b185837af8d15ae864616e0_PATTERN = re.compile(r"/v1/policy/device-admin/identity-stores")
    DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_bda58fc63575503b80c024dbe02cf547_PATTERN = re.compile(r"/v1/policy/device-admin/network-condition")
    DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_83ea4e38c44e5b1c90b19af25b88546e_PATTERN = re.compile(r"/v1/policy/device-admin/network-condition")
    DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_a3640f918edb5df99d09001ca9e12688_PATTERN = re.compile(r"/v1/policy/device-admin/network-condition/string")
    DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_b371441bddfd5d819a7aedfa215f4aeb_PATTERN = re.compile(r"/v1/policy/device-admin/network-condition/string")
    DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_037e7b011df45066b55be86033ecd17a_PATTERN = re.compile(r"/v1/policy/device-admin/network-condition/string")
    DEVICE_ADMINISTRATION_POLICY_SET_923587ed5920513e92b1728b824771cc_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set")
    DEVICE_ADMINISTRATION_POLICY_SET_5767ac3ccf225801ad8ba0bb1ad9de0b_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set")
    DEVICE_ADMINISTRATION_POLICY_SET_ed47964d442d52dca1f7da967f37b3e2_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/reset-hitcount")
    DEVICE_ADMINISTRATION_POLICY_SET_49f36918d98a546ab6ca2618d1844984_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string")
    DEVICE_ADMINISTRATION_POLICY_SET_b6cc40e0f4b45e8da5908776d124ed5a_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string")
    DEVICE_ADMINISTRATION_POLICY_SET_f602e2f88378502a8d8bca6dff274afe_PATTERN = re.compile(r"/v1/policy/device-admin/policy-set/string")
    DEVICE_ADMINISTRATION_PROFILES_8ca669963ed0563e96bb009bf14a417b_PATTERN = re.compile(r"/v1/policy/device-admin/profiles")
    DEVICE_ADMINISTRATION_SERVICE_NAMES_36e8018e15b053f39046b5bec0243d3f_PATTERN = re.compile(r"/v1/policy/device-admin/service-names")
    DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_816bf923264c53f98d5c347fa50b9c15_PATTERN = re.compile(r"/v1/policy/device-admin/time-condition")
    DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_98b30f809e275589bd7154b5b4093d3f_PATTERN = re.compile(r"/v1/policy/device-admin/time-condition")
    DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_15ffd94d339a5fea8a4777dccccb926f_PATTERN = re.compile(r"/v1/policy/device-admin/time-condition/string")
    DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_e3241242740252b2814e0b474c314e9b_PATTERN = re.compile(r"/v1/policy/device-admin/time-condition/string")
    DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_cf9f01129179555aa60c446f0a65c65a_PATTERN = re.compile(r"/v1/policy/device-admin/time-condition/string")
    NETWORK_ACCESS_AUTHENTICATION_RULES_7956d836da955609bd9a5243101f3536_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/authentication")
    NETWORK_ACCESS_AUTHENTICATION_RULES_c26e318c3c405713a55b4e162be8c890_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/authentication")
    NETWORK_ACCESS_AUTHENTICATION_RULES_362ffc5178ed53749ebcaadd1c2af785_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/authentication/reset-hitcount")
    NETWORK_ACCESS_AUTHENTICATION_RULES_85a98a9a386755939fe1f1633be33689_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/authentication/string")
    NETWORK_ACCESS_AUTHENTICATION_RULES_ec5180b8603d5cf78c13d6d3c0be18c2_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/authentication/string")
    NETWORK_ACCESS_AUTHENTICATION_RULES_da4f3b797ace547fa8f298d8c5197ce8_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/authentication/string")
    NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_9b2117ae65635dfd9c9d7042eb649261_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/exception")
    NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_2d40ae38628c51c49af42a4ede3d66d9_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/exception")
    NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_7d45668b438c59a6b92eb3c79386935b_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/exception/reset-hitcount")
    NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_d01cc518eafd5daeaf80b7e83f4d6ad1_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/exception/string")
    NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_d5c906da96395858b888f382e2ab9d79_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/exception/string")
    NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_0d60e4de79065869a39a937f02e3e885_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/exception/string")
    NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_8de9a19a8393543da5814b1dce75abf6_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/global-exception")
    NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_f9df6a3c6cf953319db3b8c36720997d_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/global-exception")
    NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_31254fb8a2895e8982180d5f9339f8e4_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/global-exception/reset-hitcount")
    NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_9b71b104d553520aafc4ce52b537a482_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/global-exception/string")
    NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_42639223458c51c99e8f35329c276126_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/global-exception/string")
    NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_61e00af18a485a9283811feb84b04843_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/global-exception/string")
    NETWORK_ACCESS_AUTHORIZATION_RULES_565fef1c1b1c53eeb784322caec31573_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/authorization")
    NETWORK_ACCESS_AUTHORIZATION_RULES_b9de636ff2e25f849f468556c53b7b9a_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/authorization")
    NETWORK_ACCESS_AUTHORIZATION_RULES_e263dfc3d6e5513fa6ae916a22d14e5d_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/authorization/reset-hitcount")
    NETWORK_ACCESS_AUTHORIZATION_RULES_b19f79dd969d5444a6ba7b2acbf0f3cf_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/authorization/string")
    NETWORK_ACCESS_AUTHORIZATION_RULES_a8c6432bf3c8523e9876c4ac9d92c8b5_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/authorization/string")
    NETWORK_ACCESS_AUTHORIZATION_RULES_0f8c47fa229d5f749f7432510709876c_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string/authorization/string")
    NETWORK_ACCESS_CONDITIONS_daaac00241cc57a1a360043cbce63df6_PATTERN = re.compile(r"/v1/policy/network-access/condition")
    NETWORK_ACCESS_CONDITIONS_36e5dd2909045a90bdce4848865662c2_PATTERN = re.compile(r"/v1/policy/network-access/condition")
    NETWORK_ACCESS_CONDITIONS_3a155387e56e5f9ba511dc4e4c9f46b4_PATTERN = re.compile(r"/v1/policy/network-access/condition/authentication")
    NETWORK_ACCESS_CONDITIONS_3e196799ee895b3981634d93ec48f58c_PATTERN = re.compile(r"/v1/policy/network-access/condition/authorization")
    NETWORK_ACCESS_CONDITIONS_9c98c10af4da50d99fb62c7097f07736_PATTERN = re.compile(r"/v1/policy/network-access/condition/condition-by-name/string")
    NETWORK_ACCESS_CONDITIONS_bbc720f738bf5b83a20de7e28e3c4c5f_PATTERN = re.compile(r"/v1/policy/network-access/condition/condition-by-name/string")
    NETWORK_ACCESS_CONDITIONS_1ccbc1ec86665500b4520ba48304eab7_PATTERN = re.compile(r"/v1/policy/network-access/condition/condition-by-name/string")
    NETWORK_ACCESS_CONDITIONS_902bf0cf46ba5b60b00176d2897fc7d3_PATTERN = re.compile(r"/v1/policy/network-access/condition/policyset")
    NETWORK_ACCESS_CONDITIONS_150027701d3053acae2eb596718a9ca3_PATTERN = re.compile(r"/v1/policy/network-access/condition/string")
    NETWORK_ACCESS_CONDITIONS_1f0d3cb73c4e59208d9ee04ffa787b3c_PATTERN = re.compile(r"/v1/policy/network-access/condition/string")
    NETWORK_ACCESS_CONDITIONS_010c97b4161c5b95a6a83b6917ce26d6_PATTERN = re.compile(r"/v1/policy/network-access/condition/string")
    NETWORK_ACCESS_DICTIONARY_1eb2cef3895d5bc68b7a28eca42ef630_PATTERN = re.compile(r"/v1/policy/network-access/dictionaries")
    NETWORK_ACCESS_DICTIONARY_7205be755dae5251bd2d8348eeebfdde_PATTERN = re.compile(r"/v1/policy/network-access/dictionaries")
    NETWORK_ACCESS_DICTIONARY_e60234354578568697b6740d08170678_PATTERN = re.compile(r"/v1/policy/network-access/dictionaries/string")
    NETWORK_ACCESS_DICTIONARY_e4f1e31aca1558f782a2cdb43853aaf2_PATTERN = re.compile(r"/v1/policy/network-access/dictionaries/string")
    NETWORK_ACCESS_DICTIONARY_2b80087f14af51d186a7bfa89f5a494b_PATTERN = re.compile(r"/v1/policy/network-access/dictionaries/string")
    NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_b47094632edd5daea17c82b5fcd812f5_PATTERN = re.compile(r"/v1/policy/network-access/dictionaries/string/attribute")
    NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_9d3034483aaa5563bb287ef0cd502130_PATTERN = re.compile(r"/v1/policy/network-access/dictionaries/string/attribute")
    NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_cb8619385d265527a56dc7a27527f3a1_PATTERN = re.compile(r"/v1/policy/network-access/dictionaries/string/attribute/string")
    NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_d2810d771d3e5ec580c39e0deb46b2b8_PATTERN = re.compile(r"/v1/policy/network-access/dictionaries/string/attribute/string")
    NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_e1725efd8ea253d1930913a85709977f_PATTERN = re.compile(r"/v1/policy/network-access/dictionaries/string/attribute/string")
    NETWORK_ACCESS_DICTIONARY_ATTRIBUTES_LIST_469345c8455c5c6fac438317f314f407_PATTERN = re.compile(r"/v1/policy/network-access/dictionaries/authentication")
    NETWORK_ACCESS_DICTIONARY_ATTRIBUTES_LIST_e86076c61aa9548dacaf5eb77e98a20c_PATTERN = re.compile(r"/v1/policy/network-access/dictionaries/authorization")
    NETWORK_ACCESS_DICTIONARY_ATTRIBUTES_LIST_5bce945bea7456fd930ee327ece18828_PATTERN = re.compile(r"/v1/policy/network-access/dictionaries/policyset")
    NETWORK_ACCESS_IDENTITY_STORES_4ef75d8c1654508aae4fc2ee9b34fabc_PATTERN = re.compile(r"/v1/policy/network-access/identity-stores")
    NETWORK_ACCESS_NETWORK_CONDITIONS_da2d8b2763ed53d9bec7f9427c4ce344_PATTERN = re.compile(r"/v1/policy/network-access/network-condition")
    NETWORK_ACCESS_NETWORK_CONDITIONS_858ad86a47e15d45ab1cc0cadc5b248f_PATTERN = re.compile(r"/v1/policy/network-access/network-condition")
    NETWORK_ACCESS_NETWORK_CONDITIONS_64faeb3bb3f25787844f6973d5a1658f_PATTERN = re.compile(r"/v1/policy/network-access/network-condition/string")
    NETWORK_ACCESS_NETWORK_CONDITIONS_5aaa481aaad35f8b8a7cbf2e063eac2b_PATTERN = re.compile(r"/v1/policy/network-access/network-condition/string")
    NETWORK_ACCESS_NETWORK_CONDITIONS_8e345ca7adb75b1bacfa42771a4d242c_PATTERN = re.compile(r"/v1/policy/network-access/network-condition/string")
    NETWORK_ACCESS_POLICY_SET_229b904117c35daf8833398c262c403d_PATTERN = re.compile(r"/v1/policy/network-access/policy-set")
    NETWORK_ACCESS_POLICY_SET_42e1af4e392c5790a01685b9687208c0_PATTERN = re.compile(r"/v1/policy/network-access/policy-set")
    NETWORK_ACCESS_POLICY_SET_678aef73e11e56edb468869d663b5e85_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/reset-hitcount")
    NETWORK_ACCESS_POLICY_SET_1fb3b6363bad54678ae56dc699e8c7e8_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string")
    NETWORK_ACCESS_POLICY_SET_4068064fa27e5a779143ed557b417535_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string")
    NETWORK_ACCESS_POLICY_SET_c1d0c2c01a5856fa8be5af8e2b07e420_PATTERN = re.compile(r"/v1/policy/network-access/policy-set/string")
    NETWORK_ACCESS_PROFILES_97b33c6c1bdf5c6b8c63835ce0298418_PATTERN = re.compile(r"/v1/policy/network-access/profiles")
    NETWORK_ACCESS_SECURITY_GROUPS_b92977dab6965e1c9fd86b96e4aa7e92_PATTERN = re.compile(r"/v1/policy/network-access/security-groups")
    NETWORK_ACCESS_SERVICE_NAMES_ca8f50a31b325fd281ae7f7b69f31d3f_PATTERN = re.compile(r"/v1/policy/network-access/service-names")
    NETWORK_ACCESS_TIME_DATE_CONDITIONS_1533f65d301c5ee3a66ac5220cac3348_PATTERN = re.compile(r"/v1/policy/network-access/time-condition")
    NETWORK_ACCESS_TIME_DATE_CONDITIONS_fc5800b01699562cb563664affdd7757_PATTERN = re.compile(r"/v1/policy/network-access/time-condition")
    NETWORK_ACCESS_TIME_DATE_CONDITIONS_e8c39503b29051bea788021a168833da_PATTERN = re.compile(r"/v1/policy/network-access/time-condition/string")
    NETWORK_ACCESS_TIME_DATE_CONDITIONS_fef057ddea8d56a98189b1db3bf5f240_PATTERN = re.compile(r"/v1/policy/network-access/time-condition/string")
    NETWORK_ACCESS_TIME_DATE_CONDITIONS_10517292296559f2847ac681d93cf40b_PATTERN = re.compile(r"/v1/policy/network-access/time-condition/string")
    ACI_BINDINGS_3d1448851f0154d0b6e9c856ec6cc6f0_PATTERN = re.compile(r"/ers/config/acibindings/getall")
    ACI_BINDINGS_d74b5214bad656c98f21e4968661c3c0_PATTERN = re.compile(r"/ers/config/acibindings/versioninfo")
    ACI_SETTINGS_2ea5c865993b56f48f7f43475294a20c_PATTERN = re.compile(r"/ers/config/acisettings")
    ACI_SETTINGS_1b155c91eec153338302d492db1afb80_PATTERN = re.compile(r"/ers/config/acisettings/testACIConnectivity")
    ACI_SETTINGS_56cea2e785ee57908a9ee3b118e49cfa_PATTERN = re.compile(r"/ers/config/acisettings/string")
    ACI_SETTINGS_462410ea47f65521bcf0ab949b5d72b5_PATTERN = re.compile(r"/ers/config/acisettings/versioninfo")
    ACTIVE_DIRECTORY_7c6be021c4ca59e48c97afe218219bb1_PATTERN = re.compile(r"/ers/config/activedirectory/name/string")
    ACTIVE_DIRECTORY_b839d4dee9b958e48ccef056603e253f_PATTERN = re.compile(r"/ers/config/activedirectory/string/getUserGroups")
    ACTIVE_DIRECTORY_14104b05e80058df96e685baa727d578_PATTERN = re.compile(r"/ers/config/activedirectory/string/addGroups")
    ACTIVE_DIRECTORY_8091e84541805d1da1fa3d4d581102a9_PATTERN = re.compile(r"/ers/config/activedirectory/string/leave")
    ACTIVE_DIRECTORY_eae60ece5110590e97ddd910e8144ed2_PATTERN = re.compile(r"/ers/config/activedirectory/string/isUserMemberOf")
    ACTIVE_DIRECTORY_7d0ed84901325292ad4e2a91a174f6b2_PATTERN = re.compile(r"/ers/config/activedirectory/string/getTrustedDomains")
    ACTIVE_DIRECTORY_e84705b918955b53afe61fc37911eb8b_PATTERN = re.compile(r"/ers/config/activedirectory/string/joinAllNodes")
    ACTIVE_DIRECTORY_d011417d18d055ccb864c1dc2ae0456d_PATTERN = re.compile(r"/ers/config/activedirectory/string/leaveAllNodes")
    ACTIVE_DIRECTORY_48fd729f50e65695966359b589a1606b_PATTERN = re.compile(r"/ers/config/activedirectory/string/getGroupsByDomain")
    ACTIVE_DIRECTORY_15236cfcc7615d0492e2dd1b04dd03a9_PATTERN = re.compile(r"/ers/config/activedirectory/string")
    ACTIVE_DIRECTORY_786febbe79ed5bb780d97a98f292b606_PATTERN = re.compile(r"/ers/config/activedirectory/string")
    ACTIVE_DIRECTORY_b3284240745e5b929c51495fe80bc1c4_PATTERN = re.compile(r"/ers/config/activedirectory/string/join")
    ACTIVE_DIRECTORY_c8dbec9679d453f78cb47d894c507a7b_PATTERN = re.compile(r"/ers/config/activedirectory")
    ACTIVE_DIRECTORY_64e9318040a456978757d7abfa3e66b1_PATTERN = re.compile(r"/ers/config/activedirectory")
    ACTIVE_DIRECTORY_c2d0923990e35be1882e4dee000254a9_PATTERN = re.compile(r"/ers/config/activedirectory/versioninfo")
    ADMIN_USER_adac9b81d9235be3b656acf9436583dd_PATTERN = re.compile(r"/ers/config/adminuser/string")
    ADMIN_USER_463a109d72fa5ac0a64d357302f26669_PATTERN = re.compile(r"/ers/config/adminuser")
    ADMIN_USER_9535a5edeb5057839d702e0f490dc28f_PATTERN = re.compile(r"/ers/config/adminuser/versioninfo")
    ALLOWED_PROTOCOLS_010ac8c8cb9b5007a1e1a6434a20a881_PATTERN = re.compile(r"/ers/config/allowedprotocols/name/string")
    ALLOWED_PROTOCOLS_696e3ddfddd45e299f14ed194926f8de_PATTERN = re.compile(r"/ers/config/allowedprotocols/string")
    ALLOWED_PROTOCOLS_61a0b312f70257b1bfa90d0260f0c971_PATTERN = re.compile(r"/ers/config/allowedprotocols/string")
    ALLOWED_PROTOCOLS_a6cbd2c420785cfcbdecc3495bca8af4_PATTERN = re.compile(r"/ers/config/allowedprotocols/string")
    ALLOWED_PROTOCOLS_d82fe0f9e4635b74af809beaaf98bd07_PATTERN = re.compile(r"/ers/config/allowedprotocols")
    ALLOWED_PROTOCOLS_1b40ad23ab0a5a7b8adade320c8912e7_PATTERN = re.compile(r"/ers/config/allowedprotocols")
    ALLOWED_PROTOCOLS_c0f61393474f5744ab0a263a232d3b96_PATTERN = re.compile(r"/ers/config/allowedprotocols/versioninfo")
    AUTHORIZATION_PROFILE_acf0372068885036baee3c4524638f31_PATTERN = re.compile(r"/ers/config/authorizationprofile/name/string")
    AUTHORIZATION_PROFILE_a69c7f1ad54e5e9cae1f871e19eed61b_PATTERN = re.compile(r"/ers/config/authorizationprofile/string")
    AUTHORIZATION_PROFILE_9cb9f26e93655e7d89995b172f6fd97f_PATTERN = re.compile(r"/ers/config/authorizationprofile/string")
    AUTHORIZATION_PROFILE_c3913dfbda305f678ede16f782762ad3_PATTERN = re.compile(r"/ers/config/authorizationprofile/string")
    AUTHORIZATION_PROFILE_2e232c5666ab5ed783588f413c3bc644_PATTERN = re.compile(r"/ers/config/authorizationprofile")
    AUTHORIZATION_PROFILE_9c43118f80d4556a8ec759a8c41e2097_PATTERN = re.compile(r"/ers/config/authorizationprofile")
    AUTHORIZATION_PROFILE_3bee8aa3a03a57a3a5eb1418fe1250b6_PATTERN = re.compile(r"/ers/config/authorizationprofile/versioninfo")
    BYOD_PORTAL_effdf30a3e3a5781ba1f5cf833395359_PATTERN = re.compile(r"/ers/config/byodportal/string")
    BYOD_PORTAL_3e38d10b1ea257d49ebce893e87b3419_PATTERN = re.compile(r"/ers/config/byodportal/string")
    BYOD_PORTAL_df2fb34fbab65254ac87d1be50abd15f_PATTERN = re.compile(r"/ers/config/byodportal/string")
    BYOD_PORTAL_41a23b580495514394b125800e073c9a_PATTERN = re.compile(r"/ers/config/byodportal")
    BYOD_PORTAL_afcce33ec863567f94f3b9b73719ff8d_PATTERN = re.compile(r"/ers/config/byodportal")
    BYOD_PORTAL_c5d2d9d8c20b58049cd3326850f2292f_PATTERN = re.compile(r"/ers/config/byodportal/versioninfo")
    CERTIFICATE_PROFILE_1d473b3690e951be9375d770225b9657_PATTERN = re.compile(r"/ers/config/certificateprofile/string")
    CERTIFICATE_PROFILE_d24a3f485ff758d099b1e4713f18f1c1_PATTERN = re.compile(r"/ers/config/certificateprofile/string")
    CERTIFICATE_PROFILE_e09287aba99c56a6a9171b7e3a635a43_PATTERN = re.compile(r"/ers/config/certificateprofile/string")
    CERTIFICATE_PROFILE_3be38700993b5f70acfdc8e44f5558d8_PATTERN = re.compile(r"/ers/config/certificateprofile")
    CERTIFICATE_PROFILE_776141419f955525b0b38a57a3bed311_PATTERN = re.compile(r"/ers/config/certificateprofile")
    CERTIFICATE_PROFILE_8e00be3b97b85829bef60c09eaa922ac_PATTERN = re.compile(r"/ers/config/certificateprofile/versioninfo")
    CERTIFICATE_TEMPLATE_e04f248274ea584aa30857975a28297f_PATTERN = re.compile(r"/ers/config/certificatetemplate/string")
    CERTIFICATE_TEMPLATE_e9e38cdf5bcb5c018b7f10f1d0864215_PATTERN = re.compile(r"/ers/config/certificatetemplate/string")
    CERTIFICATE_TEMPLATE_dc1da5c3912a5117878160e27f6b533a_PATTERN = re.compile(r"/ers/config/certificatetemplate/")
    CERTIFICATE_TEMPLATE_3f126f916efd575dbc9acae4ab2a1e4e_PATTERN = re.compile(r"/ers/config/certificatetemplate/versioninfo")
    DOWNLOADABLE_ACL_dfa8f48210e85715beebb44e62fac408_PATTERN = re.compile(r"/ers/config/downloadableacl/string")
    DOWNLOADABLE_ACL_2d8c7ba0cb8f56d99135e16d2d973d11_PATTERN = re.compile(r"/ers/config/downloadableacl/string")
    DOWNLOADABLE_ACL_42b3db444eaa50678218c29f88de60e8_PATTERN = re.compile(r"/ers/config/downloadableacl/string")
    DOWNLOADABLE_ACL_9191bc200af85d598885a990ff9bcbf8_PATTERN = re.compile(r"/ers/config/downloadableacl")
    DOWNLOADABLE_ACL_adcf947c42fe5588b7b82d9c43a3bbf0_PATTERN = re.compile(r"/ers/config/downloadableacl")
    DOWNLOADABLE_ACL_d10b7914625e5da0861cbeab4cf6440e_PATTERN = re.compile(r"/ers/config/downloadableacl/versioninfo")
    EGRESS_MATRIX_CELL_247716f503ab54e2921d713ed88f51c9_PATTERN = re.compile(r"/ers/config/egressmatrixcell/clearallmatrixcells")
    EGRESS_MATRIX_CELL_90540642f47f525dbd71ef49710ef578_PATTERN = re.compile(r"/ers/config/egressmatrixcell/status/string")
    EGRESS_MATRIX_CELL_892a1e6c05d05e67906b3b59bbe6d274_PATTERN = re.compile(r"/ers/config/egressmatrixcell/clonecell/string/srcSgt/string/dstSgt/string")
    EGRESS_MATRIX_CELL_0cdc971b23285b87945021bd5983d1cd_PATTERN = re.compile(r"/ers/config/egressmatrixcell/string")
    EGRESS_MATRIX_CELL_ce83fba942c25938bae0c7012df68317_PATTERN = re.compile(r"/ers/config/egressmatrixcell/string")
    EGRESS_MATRIX_CELL_e4393915121d5bcc94dfde6c8f6f7f1c_PATTERN = re.compile(r"/ers/config/egressmatrixcell/string")
    EGRESS_MATRIX_CELL_c5e52706e7095a81b8d32f3024e01cf6_PATTERN = re.compile(r"/ers/config/egressmatrixcell")
    EGRESS_MATRIX_CELL_64c560004d8b5f64a10f2cc070368c12_PATTERN = re.compile(r"/ers/config/egressmatrixcell")
    EGRESS_MATRIX_CELL_703c9da5c04b59358ac8bb1034340df4_PATTERN = re.compile(r"/ers/config/egressmatrixcell/versioninfo")
    EGRESS_MATRIX_CELL_aa333658bf83576eb36a025283516518_PATTERN = re.compile(r"/ers/config/egressmatrixcell/bulk/submit")
    EGRESS_MATRIX_CELL_72048face30e52b28c76c1b2574de858_PATTERN = re.compile(r"/ers/config/egressmatrixcell/bulk/string")
    ENDPOINT_CERTIFICATE_8e27d5df9cbe5b29a7e16bb7c877a4ce_PATTERN = re.compile(r"/ers/config/endpointcert/certRequest")
    ENDPOINT_CERTIFICATE_4c5c84028d8f5c078d8ab37553812d39_PATTERN = re.compile(r"/ers/config/endpointcert/versioninfo")
    ENDPOINT_IDENTITY_GROUP_2590f64c3c08518e9eef83a92d69cde3_PATTERN = re.compile(r"/ers/config/endpointgroup/name/string")
    ENDPOINT_IDENTITY_GROUP_5e4bfa620f76545d9887045cd24d99a2_PATTERN = re.compile(r"/ers/config/endpointgroup/string")
    ENDPOINT_IDENTITY_GROUP_189979b4e8d45639975c226dacd53e7b_PATTERN = re.compile(r"/ers/config/endpointgroup/string")
    ENDPOINT_IDENTITY_GROUP_f7b0aab2a65652feae637779bfb20d2d_PATTERN = re.compile(r"/ers/config/endpointgroup/string")
    ENDPOINT_IDENTITY_GROUP_cd429bb8ff3556a796570480f742028b_PATTERN = re.compile(r"/ers/config/endpointgroup")
    ENDPOINT_IDENTITY_GROUP_b14d63c641e95ac0a8c2da2fb65909c7_PATTERN = re.compile(r"/ers/config/endpointgroup")
    ENDPOINT_IDENTITY_GROUP_1d553cc3b48d5689ac45a582a5d98f9b_PATTERN = re.compile(r"/ers/config/endpointgroup/versioninfo")
    ENDPOINT_258969f4f97557daacb3dadaced526cc_PATTERN = re.compile(r"/ers/config/endpoint/string/releaserejectedendpoint")
    ENDPOINT_ed121b2686e85bd5b28c068c3c0de220_PATTERN = re.compile(r"/ers/config/endpoint/string/deregister")
    ENDPOINT_f8a2f0834e625822bed1cb4cf34fde5e_PATTERN = re.compile(r"/ers/config/endpoint/getrejectedendpoints")
    ENDPOINT_7d53842e83f0538cab91e097aa6800ce_PATTERN = re.compile(r"/ers/config/endpoint/name/string")
    ENDPOINT_eb8e0ce63376573995a49178435f7747_PATTERN = re.compile(r"/ers/config/endpoint/string")
    ENDPOINT_c8b30af4b84b5a90be2fc152cf26ad42_PATTERN = re.compile(r"/ers/config/endpoint/string")
    ENDPOINT_36658f1cac5f578ab6509196266ad8e3_PATTERN = re.compile(r"/ers/config/endpoint/string")
    ENDPOINT_dfaeea899c185169ae2a3b70b5491008_PATTERN = re.compile(r"/ers/config/endpoint/register")
    ENDPOINT_719765b7f7285d71be4645db91b0fc74_PATTERN = re.compile(r"/ers/config/endpoint")
    ENDPOINT_845787ab88be5092bf4ba9f522e8e26f_PATTERN = re.compile(r"/ers/config/endpoint")
    ENDPOINT_85adcb1d998d54838add3b4d644242af_PATTERN = re.compile(r"/ers/config/endpoint/versioninfo")
    ENDPOINT_c03505504e8e5af8a715e27c40f16eab_PATTERN = re.compile(r"/ers/config/endpoint/bulk/submit")
    ENDPOINT_5b054a43ba875f0da3da5a7d863f3ef7_PATTERN = re.compile(r"/ers/config/endpoint/bulk/string")
    EXTERNAL_RADIUS_SERVER_e6019b6b2b605132b57db142f581e710_PATTERN = re.compile(r"/externalradiusserver/name/string")
    EXTERNAL_RADIUS_SERVER_81735151a93c51c59037ec968625ee45_PATTERN = re.compile(r"/externalradiusserver/string")
    EXTERNAL_RADIUS_SERVER_28036825e94f5eba9d9615a3ecc18ebc_PATTERN = re.compile(r"/externalradiusserver/string")
    EXTERNAL_RADIUS_SERVER_373fcbde1c215f95bebbfa95780ed9a8_PATTERN = re.compile(r"/externalradiusserver/string")
    EXTERNAL_RADIUS_SERVER_9b641825a9555ecba105cabbdf50fc78_PATTERN = re.compile(r"/ers/config/externalradiusserver")
    EXTERNAL_RADIUS_SERVER_1fc1c74b35ae5050b4f7fd702570ad5b_PATTERN = re.compile(r"/ers/config/externalradiusserver")
    EXTERNAL_RADIUS_SERVER_a6c3ffe72746500b88be3a5418ead4ba_PATTERN = re.compile(r"/ers/config/externalradiusserver/versioninfo")
    FILTER_POLICY_16555f5d5ab6568d8bf5f9932f7ed7f4_PATTERN = re.compile(r"/ers/config/filterpolicy/string")
    FILTER_POLICY_95d0006cc03d53c89a3593526bf8dc0f_PATTERN = re.compile(r"/ers/config/filterpolicy/string")
    FILTER_POLICY_4a83e0d4f56a5c06946f685aa46fa3e3_PATTERN = re.compile(r"/ers/config/filterpolicy/string")
    FILTER_POLICY_250a599ae00f5e47b9ece23cd3183d1c_PATTERN = re.compile(r"/ers/config/filterpolicy")
    FILTER_POLICY_22f8082b07ce528f82545e210b84d7de_PATTERN = re.compile(r"/ers/config/filterpolicy")
    FILTER_POLICY_209810ed6cad570d90243b1e0dbbe27b_PATTERN = re.compile(r"/ers/config/filterpolicy/versioninfo")
    GUEST_LOCATION_ca2e75fbf5b45ba3b399e5616458b855_PATTERN = re.compile(r"/ers/config/guestlocation/string")
    GUEST_LOCATION_13ea10f18c3655db84657ad855bf6972_PATTERN = re.compile(r"/ers/config/guestlocation")
    GUEST_LOCATION_fdfe562af248561f981549b96f8ed397_PATTERN = re.compile(r"/ers/config/guestlocation/versioninfo")
    GUEST_SMTP_NOTIFICATION_CONFIGURATION_ca28129793d1569bb50de9f43b0d0ee8_PATTERN = re.compile(r"/ers/config/guestsmtpnotificationsettings/string")
    GUEST_SMTP_NOTIFICATION_CONFIGURATION_a7500f6e473a50e19452683e303dd021_PATTERN = re.compile(r"/ers/config/guestsmtpnotificationsettings/string")
    GUEST_SMTP_NOTIFICATION_CONFIGURATION_51e4c74e9b4e559e95c73e81183a6c7a_PATTERN = re.compile(r"/ers/config/guestsmtpnotificationsettings")
    GUEST_SMTP_NOTIFICATION_CONFIGURATION_01643de7c6f75f68b0d7df00dc72808d_PATTERN = re.compile(r"/ers/config/guestsmtpnotificationsettings")
    GUEST_SMTP_NOTIFICATION_CONFIGURATION_0a0c0e67aead55a2b4db67e9d068351a_PATTERN = re.compile(r"/ers/config/guestsmtpnotificationsettings/versioninfo")
    GUEST_SSID_d5572c56526151cb8ea42de44b2db52c_PATTERN = re.compile(r"/ers/config/guestssid/string")
    GUEST_SSID_72e6e4b7d022556a80f1948efb3d5c61_PATTERN = re.compile(r"/ers/config/guestssid/string")
    GUEST_SSID_8328407df7345f788230a512d6635c25_PATTERN = re.compile(r"/ers/config/guestssid/string")
    GUEST_SSID_c37778a2faa5552894cc60cec13c56c7_PATTERN = re.compile(r"/ers/config/guestssid")
    GUEST_SSID_2a31eb33e3535754b3f754a9199e0d25_PATTERN = re.compile(r"/ers/config/guestssid")
    GUEST_SSID_b400ebaa2d1f51398d3b32e7a6e4ba35_PATTERN = re.compile(r"/ers/config/guestssid/versioninfo")
    GUEST_TYPE_01c7aed7320e54bfac29f13c8717a6b5_PATTERN = re.compile(r"/ers/config/ers/config/guesttype/email/string")
    GUEST_TYPE_f9661f7c85c2570897cffc3d02668263_PATTERN = re.compile(r"/ers/config/ers/config/guesttype/sms/string")
    GUEST_TYPE_4acb5a41fe395b158a3fe1cda996b0cf_PATTERN = re.compile(r"/ers/config/guesttype/string")
    GUEST_TYPE_bac6d4d95ac45a0a8933b8712dcbe70d_PATTERN = re.compile(r"/ers/config/guesttype/string")
    GUEST_TYPE_6faa7211d68e5b329034e17c82b78694_PATTERN = re.compile(r"/ers/config/guesttype/string")
    GUEST_TYPE_0f41a1e47105581fabf212f259626903_PATTERN = re.compile(r"/ers/config/guesttype")
    GUEST_TYPE_f46c01449d585b088490c4db530c56d5_PATTERN = re.compile(r"/ers/config/guesttype")
    GUEST_TYPE_a6bfaedfca185fb7b6a86621e866a5f6_PATTERN = re.compile(r"/ers/config/guesttype/versioninfo")
    GUEST_USER_c67b4dcffba052ae8ece775bc61a1c21_PATTERN = re.compile(r"/ers/config/guestuser/approve/string")
    GUEST_USER_2eb3472c4de150828b2dae61e2285313_PATTERN = re.compile(r"/ers/config/guestuser/changeSponsorPassword/string")
    GUEST_USER_83983afcc8fe53b4824ae744a2ff3848_PATTERN = re.compile(r"/ers/config/guestuser/suspend/name/string")
    GUEST_USER_18b21045846d5097a82cd61cb3c7eaf1_PATTERN = re.compile(r"/ers/config/guestuser/reinstate/name/string")
    GUEST_USER_bcb7ec29968e5d5899df4a90d94ed659_PATTERN = re.compile(r"/ers/config/guestuser/name/string")
    GUEST_USER_f24049df29d059c48eef86d381ffad5d_PATTERN = re.compile(r"/ers/config/guestuser/name/string")
    GUEST_USER_76ef15d7c6b259f5859ee9675c38887c_PATTERN = re.compile(r"/ers/config/guestuser/name/string")
    GUEST_USER_7ea6ea4e41d85f83b6f6c10ce38bb9ed_PATTERN = re.compile(r"/ers/config/guestuser/resetpassword/string")
    GUEST_USER_4dfcba4a0f685c168bdf2b5b2be317ac_PATTERN = re.compile(r"/ers/config/guestuser/reinstate/string")
    GUEST_USER_9a9fa9cbccbe50fcb1cd6a63fed47578_PATTERN = re.compile(r"/ers/config/guestuser/email/string/portalId/string")
    GUEST_USER_290601ba14b751f98206ca2e19cff3fe_PATTERN = re.compile(r"/ers/config/guestuser/sms/string/portalId/string")
    GUEST_USER_3c1e5e2a187652018c59b10155ac973d_PATTERN = re.compile(r"/ers/config/guestuser/deny/string")
    GUEST_USER_2645275c3c7d5a3a83d9f7441972d399_PATTERN = re.compile(r"/ers/config/guestuser/string")
    GUEST_USER_8754551b9c7c5847b17684c49399ff95_PATTERN = re.compile(r"/ers/config/guestuser/string")
    GUEST_USER_1030e251b39f55d3ac2570a963a3ee9c_PATTERN = re.compile(r"/ers/config/guestuser/string")
    GUEST_USER_1a5abd33eeaa52e39e926472751ef79e_PATTERN = re.compile(r"/ers/config/guestuser")
    GUEST_USER_89f7cf06a1655d6da606ace9b0950bcf_PATTERN = re.compile(r"/ers/config/guestuser")
    GUEST_USER_08be5b1e320e55f4a181370417471d9e_PATTERN = re.compile(r"/ers/config/guestuser/suspend/string")
    GUEST_USER_76abe22ea0c45f619731bd568c9f57f4_PATTERN = re.compile(r"/ers/config/guestuser/versioninfo")
    GUEST_USER_37edfca30e8e514d9bab840c3c2d4c0f_PATTERN = re.compile(r"/ers/config/guestuser/bulk/submit")
    GUEST_USER_e38a1af3ad835636a11375363528fa2e_PATTERN = re.compile(r"/ers/config/guestuser/bulk/string")
    HOTSPOT_PORTAL_6cbcecf65a0155fcad602d3ac16531a7_PATTERN = re.compile(r"/ers/config/hotspotportal/string")
    HOTSPOT_PORTAL_0ae4af25df565334b20a24c4878b68e4_PATTERN = re.compile(r"/ers/config/hotspotportal/string")
    HOTSPOT_PORTAL_1a344d1c6f535789b7badbaa502e8d3b_PATTERN = re.compile(r"/ers/config/hotspotportal/string")
    HOTSPOT_PORTAL_d912b1c21e2b5dca8b56332d3a8ad13d_PATTERN = re.compile(r"/ers/config/hotspotportal")
    HOTSPOT_PORTAL_0df78c9a3f72584dbd1c7b667b0e312f_PATTERN = re.compile(r"/ers/config/hotspotportal")
    HOTSPOT_PORTAL_91257d81be4f5a0486cc085499c19b1c_PATTERN = re.compile(r"/ers/config/hotspotportal/versioninfo")
    IDENTITY_GROUPS_1f18bdd1938755409bf6db6b29e85d3a_PATTERN = re.compile(r"/ers/config/identitygroup/name/string")
    IDENTITY_GROUPS_ca3df31c13b857e6b5dbc8357a8ab010_PATTERN = re.compile(r"/ers/config/identitygroup/string")
    IDENTITY_GROUPS_1c0689e940ba5526946ad15976cc3365_PATTERN = re.compile(r"/ers/config/identitygroup/string")
    IDENTITY_GROUPS_9d904c521059563490c4a93871b33d51_PATTERN = re.compile(r"/ers/config/identitygroup")
    IDENTITY_GROUPS_592250bf19f653f9a5c48d1fb1890409_PATTERN = re.compile(r"/ers/config/identitygroup")
    IDENTITY_GROUPS_aab79aee0b455bfea8a6d7c6464a2a09_PATTERN = re.compile(r"/ers/config/identitygroup/versioninfo")
    IDENTITY_SEQUENCE_db686413cf4558188ea60ccc05c3e920_PATTERN = re.compile(r"/ers/config/idstoresequence/name/string")
    IDENTITY_SEQUENCE_45cb9345e58f5433ae80f5d8f855978b_PATTERN = re.compile(r"/ers/config/idstoresequence/string")
    IDENTITY_SEQUENCE_9c316d5e2fdd51bdab039ea9e2a417bd_PATTERN = re.compile(r"/ers/config/idstoresequence/string")
    IDENTITY_SEQUENCE_2b8258803668534d87781e995c73c23a_PATTERN = re.compile(r"/ers/config/idstoresequence/string")
    IDENTITY_SEQUENCE_feb30ca768795eed82c118d009d7bcd4_PATTERN = re.compile(r"/ers/config/idstoresequence")
    IDENTITY_SEQUENCE_6cc0a87094bf5d96af61403dfc3747db_PATTERN = re.compile(r"/ers/config/idstoresequence")
    IDENTITY_SEQUENCE_dc4c840ad93e53d591ca3a39184e6dde_PATTERN = re.compile(r"/ers/config/idstoresequence/versioninfo")
    INTERNAL_USER_7f403dda9440503191536993f569cc6f_PATTERN = re.compile(r"/ers/config/internaluser/name/string")
    INTERNAL_USER_4758008519d9509db339e3b27dc56b37_PATTERN = re.compile(r"/ers/config/internaluser/name/string")
    INTERNAL_USER_2447b4e2fc3e595aa1be86d6589614b9_PATTERN = re.compile(r"/ers/config/internaluser/name/string")
    INTERNAL_USER_bacf1abfc35e509183c9a7f055cbbfec_PATTERN = re.compile(r"/ers/config/internaluser/string")
    INTERNAL_USER_f7227b280b745b94bb801369b168a529_PATTERN = re.compile(r"/ers/config/internaluser/string")
    INTERNAL_USER_dcf28db5184e51139b15f9ffccd10b67_PATTERN = re.compile(r"/ers/config/internaluser/string")
    INTERNAL_USER_3ccba98a61555ae495f6a05284e3b5ae_PATTERN = re.compile(r"/ers/config/internaluser")
    INTERNAL_USER_bf175c04fcb051b9a6fd70a2252903fa_PATTERN = re.compile(r"/ers/config/internaluser")
    INTERNAL_USER_2af99828533e58a2b84996b85bacc9ff_PATTERN = re.compile(r"/ers/config/internaluser/versioninfo")
    IP_TO_SGT_MAPPING_GROUP_bd7f3fb27d71596ebafecca578c85bc7_PATTERN = re.compile(r"/ers/config/sgmappinggroup/string/deploy")
    IP_TO_SGT_MAPPING_GROUP_0b8ef94d6d5554a4b57d37c52612ad7d_PATTERN = re.compile(r"/ers/config/sgmappinggroup/deployall")
    IP_TO_SGT_MAPPING_GROUP_d6c25690e3a854c5be7763a4106e379e_PATTERN = re.compile(r"/ers/config/sgmappinggroup/deploy/status")
    IP_TO_SGT_MAPPING_GROUP_e56b94dafa5652228fd71abd2b4d6df3_PATTERN = re.compile(r"/ers/config/sgmappinggroup/string")
    IP_TO_SGT_MAPPING_GROUP_02a5a26c964e53b3be3f9f0c103f304c_PATTERN = re.compile(r"/ers/config/sgmappinggroup/string")
    IP_TO_SGT_MAPPING_GROUP_73ebc15160cf5c0184d3eaff3be14508_PATTERN = re.compile(r"/ers/config/sgmappinggroup/string")
    IP_TO_SGT_MAPPING_GROUP_680a1544a7125003b7803c0ed383f4bf_PATTERN = re.compile(r"/ers/config/sgmappinggroup")
    IP_TO_SGT_MAPPING_GROUP_55c2e3af6da356009f6499f00a4115e9_PATTERN = re.compile(r"/ers/config/sgmappinggroup")
    IP_TO_SGT_MAPPING_GROUP_14c9a2546739540eb2c1cb7c411836cb_PATTERN = re.compile(r"/ers/config/sgmappinggroup/versioninfo")
    IP_TO_SGT_MAPPING_GROUP_a39fa17ffcd45736aa221dd27916e843_PATTERN = re.compile(r"/ers/config/sgmappinggroup/bulk/submit")
    IP_TO_SGT_MAPPING_GROUP_bb5f9095ca7953d3bdb16155e263f25a_PATTERN = re.compile(r"/ers/config/sgmappinggroup/bulk/string")
    IP_TO_SGT_MAPPING_b5711af534e557749661afb5b6c90cee_PATTERN = re.compile(r"/ers/config/sgmapping/string/deploy")
    IP_TO_SGT_MAPPING_83343989df7a50feb38d8729b99553e9_PATTERN = re.compile(r"/ers/config/sgmapping/deployall")
    IP_TO_SGT_MAPPING_dcd55e1e57d25e65b625526a1d341afd_PATTERN = re.compile(r"/ers/config/sgmapping/deploy/status")
    IP_TO_SGT_MAPPING_17ddc6729af25f8b8c060b20d09f0057_PATTERN = re.compile(r"/ers/config/sgmapping/string")
    IP_TO_SGT_MAPPING_94de3cecd62e5153881245a8613fbeea_PATTERN = re.compile(r"/ers/config/sgmapping/string")
    IP_TO_SGT_MAPPING_582650f0cb1e55c9baee89c136c8ec47_PATTERN = re.compile(r"/ers/config/sgmapping/string")
    IP_TO_SGT_MAPPING_10cd9e91565f5c74b9f32ff0e5be6f17_PATTERN = re.compile(r"/ers/config/sgmapping")
    IP_TO_SGT_MAPPING_52dd838b268f5dd298a123ac58448ea9_PATTERN = re.compile(r"/ers/config/sgmapping")
    IP_TO_SGT_MAPPING_63042762af0b5041b56b12c5c08cc53e_PATTERN = re.compile(r"/ers/config/sgmapping/versioninfo")
    IP_TO_SGT_MAPPING_ab203a1dd0015924bf2005a84ae85477_PATTERN = re.compile(r"/ers/config/sgmapping/bulk/submit")
    IP_TO_SGT_MAPPING_9f36d3f43a6157978ec529318ce506e0_PATTERN = re.compile(r"/ers/config/sgmapping/bulk/string")
    MY_DEVICE_PORTAL_4bb3528d280652678f8e211b9e418e66_PATTERN = re.compile(r"/ers/config/mydeviceportal/string")
    MY_DEVICE_PORTAL_83079c64b769537ea7c586565f6ed2a2_PATTERN = re.compile(r"/ers/config/mydeviceportal/string")
    MY_DEVICE_PORTAL_c04f18d6afee5f649a5700bf3074adb9_PATTERN = re.compile(r"/ers/config/mydeviceportal/string")
    MY_DEVICE_PORTAL_90a71ccf29f05ee29af909b07bb9c754_PATTERN = re.compile(r"/ers/config/mydeviceportal")
    MY_DEVICE_PORTAL_e643a5ac8bca55f58ea8d6260c57eafe_PATTERN = re.compile(r"/ers/config/mydeviceportal")
    MY_DEVICE_PORTAL_5e356376df735e72aa55332951806f42_PATTERN = re.compile(r"/ers/config/mydeviceportal/versioninfo")
    NATIVE_SUPPLICANT_PROFILE_5d1b9755414c5dcbb61987b2dd06839a_PATTERN = re.compile(r"/ers/config/nspprofile/string")
    NATIVE_SUPPLICANT_PROFILE_c54a2ad63f46527dbec140a05f1213b7_PATTERN = re.compile(r"/ers/config/nspprofile/string")
    NATIVE_SUPPLICANT_PROFILE_3fff9d421c78597d98a54dd08a9a99f9_PATTERN = re.compile(r"/ers/config/nspprofile/string")
    NATIVE_SUPPLICANT_PROFILE_6470fa9802505d7bbdf85b951581db47_PATTERN = re.compile(r"/ers/config/nspprofile")
    NATIVE_SUPPLICANT_PROFILE_f577c55d36b05178b0275dd88c71e118_PATTERN = re.compile(r"/ers/config/nspprofile/versioninfo")
    NETWORK_DEVICE_GROUP_e1d938f110e059a5abcb9cc8fb3cbd7c_PATTERN = re.compile(r"/ers/config/networkdevicegroup/name/string")
    NETWORK_DEVICE_GROUP_a0fdb67d95475cd39382171dec96d6c1_PATTERN = re.compile(r"/ers/config/networkdevicegroup/string")
    NETWORK_DEVICE_GROUP_808461e6734850fabb2097fa969948cb_PATTERN = re.compile(r"/ers/config/networkdevicegroup/string")
    NETWORK_DEVICE_GROUP_9291975ded6653128f502c97e52cf279_PATTERN = re.compile(r"/ers/config/networkdevicegroup/string")
    NETWORK_DEVICE_GROUP_2a1af553d663556ca429a10ed82effda_PATTERN = re.compile(r"/ers/config/networkdevicegroup")
    NETWORK_DEVICE_GROUP_6c38fb2e2dd45f4dab6ec3a19effd15a_PATTERN = re.compile(r"/ers/config/networkdevicegroup")
    NETWORK_DEVICE_GROUP_163f22d64bd4557d856a66ad6599d2d1_PATTERN = re.compile(r"/ers/config/networkdevicegroup/versioninfo")
    NETWORK_DEVICE_54d8610d4a355b63aaaa364447d5fa00_PATTERN = re.compile(r"/ers/config/networkdevice/name/string")
    NETWORK_DEVICE_2ea2c4586b845888b2a9375126f70de2_PATTERN = re.compile(r"/ers/config/networkdevice/name/string")
    NETWORK_DEVICE_116eafaf2e785c6898fb982dbe4462e7_PATTERN = re.compile(r"/ers/config/networkdevice/name/string")
    NETWORK_DEVICE_a4ab683ce53052e089626a096abaf451_PATTERN = re.compile(r"/ers/config/networkdevice/string")
    NETWORK_DEVICE_b1edfeb182025176bb250633937177ae_PATTERN = re.compile(r"/ers/config/networkdevice/string")
    NETWORK_DEVICE_9f2fd3c6324b581ca0f3f9eadede1cdc_PATTERN = re.compile(r"/ers/config/networkdevice/string")
    NETWORK_DEVICE_48b986fa0f0d54ef98eb135eeb88808a_PATTERN = re.compile(r"/ers/config/networkdevice")
    NETWORK_DEVICE_574ca6ab8ec556c3bc9531dc380b230a_PATTERN = re.compile(r"/ers/config/networkdevice")
    NETWORK_DEVICE_682601e571185718b6ef6e78bfbfdf68_PATTERN = re.compile(r"/ers/config/networkdevice/versioninfo")
    NETWORK_DEVICE_63b2eebd5c245e58a503aa53115eec53_PATTERN = re.compile(r"/ers/config/networkdevice/bulk/submit")
    NETWORK_DEVICE_1bf96800cc265b5e9e1566ec7088619c_PATTERN = re.compile(r"/ers/config/networkdevice/bulk/string")
    PORTAL_GLOBAL_SETTING_0ac243ecb8c157658a4bcfe77a102c14_PATTERN = re.compile(r"/ers/config/portalglobalsetting/string")
    PORTAL_GLOBAL_SETTING_c97e7851003e5a63a2a8005ac8807dc7_PATTERN = re.compile(r"/ers/config/portalglobalsetting/string")
    PORTAL_GLOBAL_SETTING_e9ce4a1e1cf955f098343646760e9d58_PATTERN = re.compile(r"/ers/config/portalglobalsetting")
    PORTAL_GLOBAL_SETTING_a9a99c0aacce5a8181e2ff79bf99ae20_PATTERN = re.compile(r"/ers/config/portalglobalsetting/versioninfo")
    PORTAL_THEME_6e58eabefef15feb880ecfe2906d805f_PATTERN = re.compile(r"/ers/config/portaltheme/string")
    PORTAL_THEME_c82dcf6f2c3d5d399045050b02208db2_PATTERN = re.compile(r"/ers/config/portaltheme/string")
    PORTAL_THEME_8567c39e537955888cc23e4f90e6449b_PATTERN = re.compile(r"/ers/config/portaltheme/string")
    PORTAL_THEME_5ad233598ed75e0c97ddd3c3f1af50e4_PATTERN = re.compile(r"/ers/config/portaltheme")
    PORTAL_THEME_91eb833980f55025bfacbfcb8de814c8_PATTERN = re.compile(r"/ers/config/portaltheme")
    PORTAL_THEME_b6bf4f02759a5e7f968896a30575e4c6_PATTERN = re.compile(r"/ers/config/portaltheme/versioninfo")
    PORTAL_5ce70db7732c596aa82bd7d1725ac02d_PATTERN = re.compile(r"/ers/config/portal/string")
    PORTAL_2a72ae8af1075d0c94912b008003b13e_PATTERN = re.compile(r"/ers/config/portal")
    PORTAL_1d754ad0697d54c98c2690c5043e0be6_PATTERN = re.compile(r"/ers/config/portal/versioninfo")
    PROFILER_PROFILE_0e176356698b5ec49609504a530c1d8a_PATTERN = re.compile(r"/ers/config/profilerprofile/string")
    PROFILER_PROFILE_688d53f6d85a5d609d49bd38cfd65e57_PATTERN = re.compile(r"/ers/config/profilerprofile")
    PROFILER_PROFILE_de35c041dc1456cca42b7b2e32a4713d_PATTERN = re.compile(r"/ers/config/profilerprofile/versioninfo")
    PX_GRID_SETTINGS_787126e5dd9b5979a409b9f456265db0_PATTERN = re.compile(r"/ers/config/pxgridsettings/autoapprove")
    PX_GRID_SETTINGS_bea00c7a4f9b5e1798ea078e123ff016_PATTERN = re.compile(r"/ers/config/pxgridsettings/versioninfo")
    RADIUS_SERVER_SEQUENCE_0d1df0e230765104863b8d63d5beb68e_PATTERN = re.compile(r"/ers/config/radiusserversequence/string")
    RADIUS_SERVER_SEQUENCE_df9ab8ff636353279d5c787585dcb6af_PATTERN = re.compile(r"/ers/config/radiusserversequence/string")
    RADIUS_SERVER_SEQUENCE_815b13838fa75d6e8d970f6eeb6a4510_PATTERN = re.compile(r"/ers/config/radiusserversequence/string")
    RADIUS_SERVER_SEQUENCE_c6c330dace185a548f70f4e5d67776ea_PATTERN = re.compile(r"/ers/config/radiusserversequence")
    RADIUS_SERVER_SEQUENCE_83ad6ca0642c5750af6ca9905721a9d7_PATTERN = re.compile(r"/ers/config/radiusserversequence")
    RADIUS_SERVER_SEQUENCE_8fb1a72ded19590fa0aa85fc59ea8cfc_PATTERN = re.compile(r"/ers/config/radiusserversequence/versioninfo")
    RESTID_STORE_17a5f22fc961547f93976a53949cac73_PATTERN = re.compile(r"/ers/config/ers/config/restidstore/name/string")
    RESTID_STORE_c85464a04f0e5ddc99f8e6b8ed0f7eac_PATTERN = re.compile(r"/ers/config/ers/config/restidstore/name/string")
    RESTID_STORE_e068a8dc1ed65f8d9cdfa70a49f543e0_PATTERN = re.compile(r"/ers/config/ers/config/restidstore/name/string")
    RESTID_STORE_788cba3f7ace597da668acfbe00364be_PATTERN = re.compile(r"/ers/config/restidstore/string")
    RESTID_STORE_ded7f8573c255c318bb1f04bfdbf01e1_PATTERN = re.compile(r"/ers/config/restidstore/string")
    RESTID_STORE_2e77a1dd4aa75dcebbc3ee4e94a162b4_PATTERN = re.compile(r"/ers/config/restidstore/string")
    RESTID_STORE_d810359e31e453ac8145981b7d5bb7e4_PATTERN = re.compile(r"/ers/config/restidstore")
    RESTID_STORE_1073c23243c950f29b51f502c03d7058_PATTERN = re.compile(r"/ers/config/restidstore")
    RESTID_STORE_1b8c3846fcf751e4b008eb0a011dea4d_PATTERN = re.compile(r"/ers/config/restidstore/versioninfo")
    SECURITY_GROUPS_ACLS_a50d1bd34d5f593aadf8eb02083c67b0_PATTERN = re.compile(r"/ers/config/sgacl/string")
    SECURITY_GROUPS_ACLS_afc81cd1e25c50319f75606b97c23b3d_PATTERN = re.compile(r"/ers/config/sgacl/string")
    SECURITY_GROUPS_ACLS_b0a2bea8bfec52b68663ef3f7ac6d7a7_PATTERN = re.compile(r"/ers/config/sgacl/string")
    SECURITY_GROUPS_ACLS_999b22d6ad9f595ab7e3eee5cf44de8a_PATTERN = re.compile(r"/ers/config/sgacl")
    SECURITY_GROUPS_ACLS_9ab61f24bdaf508590f7686e1130913f_PATTERN = re.compile(r"/ers/config/sgacl")
    SECURITY_GROUPS_ACLS_6704e67a1131578aa794d8377da9a1de_PATTERN = re.compile(r"/ers/config/sgacl/versioninfo")
    SECURITY_GROUPS_ACLS_bfff136597e25df5ae1d135251fee263_PATTERN = re.compile(r"/ers/config/sgacl/submit")
    SECURITY_GROUPS_ACLS_07af5ee576605a5a915d888924c1e804_PATTERN = re.compile(r"/ers/config/sgacl/bulk/string")
    SECURITY_GROUP_TO_VIRTUAL_NETWORK_2112393ea0a65da3ae0346b912a9efac_PATTERN = re.compile(r"/ers/config/sgtvnvlan/string")
    SECURITY_GROUP_TO_VIRTUAL_NETWORK_eae98db0c24b5ecca77cce8279e20785_PATTERN = re.compile(r"/ers/config/sgtvnvlan/string")
    SECURITY_GROUP_TO_VIRTUAL_NETWORK_9462680497c852dbb953860bef3326e0_PATTERN = re.compile(r"/ers/config/sgtvnvlan/string")
    SECURITY_GROUP_TO_VIRTUAL_NETWORK_e51b6e745cdb5bdda4de26a27b8d92bb_PATTERN = re.compile(r"/ers/config/sgtvnvlan")
    SECURITY_GROUP_TO_VIRTUAL_NETWORK_97830a0710ba581da4d3fd00e84d59e3_PATTERN = re.compile(r"/ers/config/sgtvnvlan")
    SECURITY_GROUP_TO_VIRTUAL_NETWORK_7b2811387f4e55c8839c94ea241a3236_PATTERN = re.compile(r"/ers/config/sgtvnvlan/versioninfo")
    SECURITY_GROUP_TO_VIRTUAL_NETWORK_0ff196187ee45a92bf195593ab8f102e_PATTERN = re.compile(r"/ers/config/sgtvnvlan/submit")
    SECURITY_GROUP_TO_VIRTUAL_NETWORK_10ea793a0b1b5ac498f7bc74a0aba257_PATTERN = re.compile(r"/ers/config/sgtvnvlan/bulk/string")
    SECURITY_GROUPS_ea658190e73c5ce1b27e7def4aea28e3_PATTERN = re.compile(r"/ers/config/sgt/string")
    SECURITY_GROUPS_42ce666e64a958229cfd8da70945935e_PATTERN = re.compile(r"/ers/config/sgt/string")
    SECURITY_GROUPS_ed2c0f81f4ea5299840089761bfd4f62_PATTERN = re.compile(r"/ers/config/sgt/string")
    SECURITY_GROUPS_b3c356cfc48a5da4b13b8ecbae5748b7_PATTERN = re.compile(r"/ers/config/sgt")
    SECURITY_GROUPS_1d0290eb241f5bd79221afc8d6cb32da_PATTERN = re.compile(r"/ers/config/sgt")
    SECURITY_GROUPS_ad87f41ef4845f19a19bfadac0928ae6_PATTERN = re.compile(r"/ers/config/sgt/versioninfo")
    SECURITY_GROUPS_fe0ac7fc07885c6f877768654aefd189_PATTERN = re.compile(r"/ers/config/sgt/submit")
    SECURITY_GROUPS_a3148b789a935070b99caed1e99592cf_PATTERN = re.compile(r"/ers/config/sgt/bulk/string")
    SELF_REGISTERED_PORTAL_f9c9a5e917af53dbbb91733e82e72ebe_PATTERN = re.compile(r"/ers/config/selfregportal/string")
    SELF_REGISTERED_PORTAL_400c4fada6c558d9aba09cc373d5b266_PATTERN = re.compile(r"/ers/config/selfregportal/string")
    SELF_REGISTERED_PORTAL_673f9ada2e275fa2934fdb4825266a2c_PATTERN = re.compile(r"/ers/config/selfregportal/string")
    SELF_REGISTERED_PORTAL_bb165bd00a6653ac9da440f23ee62ecc_PATTERN = re.compile(r"/ers/config/selfregportal")
    SELF_REGISTERED_PORTAL_d524614e122d53d68324daf1681eb753_PATTERN = re.compile(r"/ers/config/selfregportal")
    SELF_REGISTERED_PORTAL_3d8cc0e6962558c58d263f53b857cff0_PATTERN = re.compile(r"/ers/config/selfregportal/versioninfo")
    SMS_PROVIDER_17daac88943a5cd2bd745c483448e231_PATTERN = re.compile(r"/ers/config/smsprovider")
    SMS_PROVIDER_37250017e20e5400a53280d52487ecd6_PATTERN = re.compile(r"/ers/config/smsprovider/versioninfo")
    SPONSOR_GROUP_MEMBER_020659d6b1385f4cb9381c13a1fa4356_PATTERN = re.compile(r"/ers/config/sponsorgroupmember")
    SPONSOR_GROUP_MEMBER_0f7c916a2e265c11b8b8535e8f88c7d1_PATTERN = re.compile(r"/ers/config/sponsorgroupmember/versioninfo")
    SPONSOR_GROUP_eaa0d7c339d152b688876c2e10f51fe7_PATTERN = re.compile(r"/ers/config/sponsorgroup/string")
    SPONSOR_GROUP_dfc44f7f24d153d789efa48e904b3832_PATTERN = re.compile(r"/ers/config/sponsorgroup/string")
    SPONSOR_GROUP_61c28a45acf05fec98879d8d2ac51129_PATTERN = re.compile(r"/ers/config/sponsorgroup/string")
    SPONSOR_GROUP_f1196f1f6fde5978b0522f096926d443_PATTERN = re.compile(r"/ers/config/sponsorgroup")
    SPONSOR_GROUP_56311acd30d35ee2ae16ff23757de7d8_PATTERN = re.compile(r"/ers/config/sponsorgroup")
    SPONSOR_GROUP_e8d4001b740751e08cfc19e1fdc5fddf_PATTERN = re.compile(r"/ers/config/sponsorgroup/versioninfo")
    SPONSOR_PORTAL_cd6793a4a8e7576c8b290bdc88001f6f_PATTERN = re.compile(r"/ers/config/sponsorportal/string")
    SPONSOR_PORTAL_bd8691c5d9435e48a3c7a08658bda585_PATTERN = re.compile(r"/ers/config/sponsorportal/string")
    SPONSOR_PORTAL_d8d4c7451f7f5e2faae4e8ac530b5f08_PATTERN = re.compile(r"/ers/config/sponsorportal/string")
    SPONSOR_PORTAL_69aa24c1260a568b93c283ecd2c3510e_PATTERN = re.compile(r"/ers/config/sponsorportal")
    SPONSOR_PORTAL_1f15d19b858d59218ab56b7323ca2fae_PATTERN = re.compile(r"/ers/config/sponsorportal")
    SPONSOR_PORTAL_fa39b9cc4834522395edcbe0d6830ae4_PATTERN = re.compile(r"/ers/config/sponsorportal/versioninfo")
    SPONSORED_GUEST_PORTAL_56d1132a216d54d091022aec0ad018f8_PATTERN = re.compile(r"/ers/config/sponsoredguestportal/string")
    SPONSORED_GUEST_PORTAL_0d39172f68fd5cbd897f03f1440f98a4_PATTERN = re.compile(r"/ers/config/sponsoredguestportal/string")
    SPONSORED_GUEST_PORTAL_9218749931f05e2ebc796f080892085f_PATTERN = re.compile(r"/ers/config/sponsoredguestportal/string")
    SPONSORED_GUEST_PORTAL_97886854bdae59219027b4d40b94fa3d_PATTERN = re.compile(r"/ers/config/sponsoredguestportal")
    SPONSORED_GUEST_PORTAL_ca78559d8a9f559c87f53ea85169a2c7_PATTERN = re.compile(r"/ers/config/sponsoredguestportal")
    SPONSORED_GUEST_PORTAL_2f1aacc5c48654cebbc4d075dc7dde80_PATTERN = re.compile(r"/ers/config/sponsoredguestportal/versioninfo")
    SXP_CONNECTIONS_86a5b160a5675039b7ddf3dc960c7968_PATTERN = re.compile(r"/ers/config/sxpconnections/string")
    SXP_CONNECTIONS_1cab8440e21553c3a807d23d05e5e1aa_PATTERN = re.compile(r"/ers/config/sxpconnections/string")
    SXP_CONNECTIONS_65954377fb665776b98ba815b52515a6_PATTERN = re.compile(r"/ers/config/sxpconnections/string")
    SXP_CONNECTIONS_7c56dfcff6285f9b882c884873d5d6c1_PATTERN = re.compile(r"/ers/config/sxpconnections")
    SXP_CONNECTIONS_789c371214c759f791c0a522b9eaf5b5_PATTERN = re.compile(r"/ers/config/sxpconnections")
    SXP_CONNECTIONS_c1ceea62877152f6a4cf7ce709f4d0f8_PATTERN = re.compile(r"/ers/config/sxpconnections/versioninfo")
    SXP_CONNECTIONS_a9d9ce4538605d439015d3ed7ef88c41_PATTERN = re.compile(r"/ers/config/sxpconnections/submit")
    SXP_CONNECTIONS_9462c2fb20ca5eb79facdda896457507_PATTERN = re.compile(r"/ers/config/sxpconnections/bulk/string")
    SXP_LOCAL_BINDINGS_e56bea5248a25f799b02fcb6098a7b10_PATTERN = re.compile(r"/ers/config/sxplocalbindings/string")
    SXP_LOCAL_BINDINGS_313e07cb8ea65820863cce345c67926b_PATTERN = re.compile(r"/ers/config/sxplocalbindings/string")
    SXP_LOCAL_BINDINGS_77db04edfe595fbba5b49eb71dcb65bd_PATTERN = re.compile(r"/ers/config/sxplocalbindings/string")
    SXP_LOCAL_BINDINGS_91f845bd746a5c00967fe66178c5edbf_PATTERN = re.compile(r"/ers/config/sxplocalbindings")
    SXP_LOCAL_BINDINGS_84610cf67e0155eab895b50d1a377f21_PATTERN = re.compile(r"/ers/config/sxplocalbindings")
    SXP_LOCAL_BINDINGS_ee22235f36835dec897ed6381e3e15fc_PATTERN = re.compile(r"/ers/config/sxplocalbindings/versioninfo")
    SXP_LOCAL_BINDINGS_2b97435f47305f5da136a0d68ac6d466_PATTERN = re.compile(r"/ers/config/sxplocalbindings/submit")
    SXP_LOCAL_BINDINGS_475db866e1125ca0b7cd7cc13ac4bdd4_PATTERN = re.compile(r"/ers/config/sxplocalbindings/bulk/string")
    SXP_VPNS_cd59f40aa9305587b69944a9c819f7a9_PATTERN = re.compile(r"/ers/config/sxpvpns/string")
    SXP_VPNS_8a0501930cc9517ea1cb4103db6e0af7_PATTERN = re.compile(r"/ers/config/sxpvpns/string")
    SXP_VPNS_2a93d058764b51dc922e41bbe4ff7cd6_PATTERN = re.compile(r"/ers/config/sxpvpns")
    SXP_VPNS_1a693347bdd15bb19d69a75f088498ce_PATTERN = re.compile(r"/ers/config/sxpvpns")
    SXP_VPNS_36ca67bf525555b086ecee4cb93e9aee_PATTERN = re.compile(r"/ers/config/sxpvpns/versioninfo")
    SXP_VPNS_be45eed0938a5143bf85ffd5fd4205d0_PATTERN = re.compile(r"/ers/config/sxpvpns/submit")
    SXP_VPNS_ba771c958ccc5f499c3a819fb2c67f57_PATTERN = re.compile(r"/ers/config/sxpvpns/bulk/string")
    SYSTEM_CERTIFICATE_dd469dcee9445c72a3861ef94fb3b096_PATTERN = re.compile(r"/ers/config/systemcertificate")
    SYSTEM_CERTIFICATE_3512a19fb8fe5fe9b069aa19d2dd74d5_PATTERN = re.compile(r"/ers/config/systemcertificate/versioninfo")
    TACACS_COMMAND_SETS_34f8ba0e97135ca6bacff94d5a76df97_PATTERN = re.compile(r"/ers/config/tacacscommandsets/name/string")
    TACACS_COMMAND_SETS_2caefe2cb042513ab4a4a76f227330cb_PATTERN = re.compile(r"/ers/config/tacacscommandsets/string")
    TACACS_COMMAND_SETS_20eb6323be425816a4116eea48f16f4b_PATTERN = re.compile(r"/ers/config/tacacscommandsets/string")
    TACACS_COMMAND_SETS_4a319a83b14252eba0f00bb4c4ab0d7c_PATTERN = re.compile(r"/ers/config/tacacscommandsets/string")
    TACACS_COMMAND_SETS_c9a67d3e9015580f93a52627f19e9916_PATTERN = re.compile(r"/ers/config/tacacscommandsets")
    TACACS_COMMAND_SETS_d9cc879878ee5a34ac1c32f2f0cb8c6d_PATTERN = re.compile(r"/ers/config/tacacscommandsets")
    TACACS_COMMAND_SETS_5865f0adb7f554eb810687bd8699149a_PATTERN = re.compile(r"/ers/config/tacacscommandsets/versioninfo")
    TACACS_EXTERNAL_SERVERS_afe1108b1a59539ebe3de3e5652c9653_PATTERN = re.compile(r"/ers/config/tacacsexternalservers/name/string")
    TACACS_EXTERNAL_SERVERS_8b9eb9547216547cab8b9e686eee674b_PATTERN = re.compile(r"/ers/config/tacacsexternalservers/string")
    TACACS_EXTERNAL_SERVERS_7a7cffe3bfae55aa81b7b4447519e4cd_PATTERN = re.compile(r"/ers/config/tacacsexternalservers/string")
    TACACS_EXTERNAL_SERVERS_896816622564523798353b885b115048_PATTERN = re.compile(r"/ers/config/tacacsexternalservers/string")
    TACACS_EXTERNAL_SERVERS_8c6c2a4908ee5f48b7e9cae7572f6a94_PATTERN = re.compile(r"/ers/config/tacacsexternalservers")
    TACACS_EXTERNAL_SERVERS_b5097e4db7505ba390914b50b1c2046b_PATTERN = re.compile(r"/ers/config/tacacsexternalservers")
    TACACS_EXTERNAL_SERVERS_d3e106d187b35547bf1f0463e4fc832f_PATTERN = re.compile(r"/ers/config/tacacsexternalservers/versioninfo")
    TACACS_PROFILE_3578b8696d875b12b0a3ab735b397d7a_PATTERN = re.compile(r"/ers/config/tacacsprofile/name/string")
    TACACS_PROFILE_bdea52558473565c9963ec14c65727b8_PATTERN = re.compile(r"/ers/config/tacacsprofile/string")
    TACACS_PROFILE_4a0db9ec45c05879a6f016a1edf54793_PATTERN = re.compile(r"/ers/config/tacacsprofile/string")
    TACACS_PROFILE_9fd38182c505549fbc0d8c1122c1f685_PATTERN = re.compile(r"/ers/config/tacacsprofile/string")
    TACACS_PROFILE_ffff1c792bf559ebb39b789421be6966_PATTERN = re.compile(r"/ers/config/tacacsprofile")
    TACACS_PROFILE_c094086382485201ad36d4641fc6822e_PATTERN = re.compile(r"/ers/config/tacacsprofile")
    TACACS_PROFILE_17b22259a4415709a97bd2b7646f734f_PATTERN = re.compile(r"/ers/config/tacacsprofile/versioninfo")
    TACACS_SERVER_SEQUENCE_493b03900a2e5027b615d9f1bdcf9f63_PATTERN = re.compile(r"/ers/config/tacacsserversequence/name/string")
    TACACS_SERVER_SEQUENCE_8b9eb9547216547cab8b9e686eee674b_PATTERN = re.compile(r"/ers/config/tacacsexternalservers/string")
    TACACS_SERVER_SEQUENCE_7a7cffe3bfae55aa81b7b4447519e4cd_PATTERN = re.compile(r"/ers/config/tacacsexternalservers/string")
    TACACS_SERVER_SEQUENCE_896816622564523798353b885b115048_PATTERN = re.compile(r"/ers/config/tacacsexternalservers/string")
    TACACS_SERVER_SEQUENCE_54187c189f2f5f6b8bab3931c206c949_PATTERN = re.compile(r"/ers/config/tacacsserversequence")
    TACACS_SERVER_SEQUENCE_5902a1e26e595667bd98f84dd29232e2_PATTERN = re.compile(r"/ers/config/tacacsserversequence")
    TACACS_SERVER_SEQUENCE_aa8e1dc47a445d44ab86020f421ee721_PATTERN = re.compile(r"/ers/config/tacacsserversequence/versioninfo")
    TELEMETRY_INFORMATION_13891f52605b5f6481f6a99ec8a7e8e6_PATTERN = re.compile(r"/ers/config/telemetryinfo/string")
    TELEMETRY_INFORMATION_8f1a8ae602c95ac08676391c374274f2_PATTERN = re.compile(r"/ers/config/telemetryinfo")
    TELEMETRY_INFORMATION_86338cd5bfb6540cb70f4bc100a96aed_PATTERN = re.compile(r"/ers/config/telemetryinfo/versioninfo")
    MISC_0e629f554fa652d980ff08988c788c57_PATTERN = re.compile(r"/admin/API/mnt/Session/ActiveCount")
    MISC_6a6c71a1e4d2597ea1b5533e9f1b438f_PATTERN = re.compile(r"/admin/API/mnt/Session/ActiveList")
    MISC_2d91e71e5b84583fb8ea91fcd9fb6751_PATTERN = re.compile(r"/admin/API/mnt/Session/AuthList/null/null")
    MISC_83d51ebdbbc75c0f8ed6161ae070a276_PATTERN = re.compile(r"/admin/API/mnt/Session/PostureCount")
    MISC_1bdb77066ba75002bd343de0e9120b86_PATTERN = re.compile(r"/admin/API/mnt/Session/ProfilerCount")
    MISC_b93e1accc1f35864b9a5b7bc478c7a7c_PATTERN = re.compile(r"/admin/API/mnt/Session/MACAddress/string")
    MISC_8329e037613954b58692d89d64eba681_PATTERN = re.compile(r"/admin/API/mnt/Session/UserName/string")
    MISC_323fb7171efd5df8a0fe319983882265_PATTERN = re.compile(r"/admin/API/mnt/Session/IPAddress/string")
    MISC_123c7f72c6db5ecbb380133c106d0566_PATTERN = re.compile(r"/admin/API/mnt/Session/EndPointIPAddress/string")
    MISC_4eb415db854f5b12aa326bde54285c59_PATTERN = re.compile(r"/admin/API/mnt/Session/Active/SessionID/string/0")
    MISC_549bd2a2c3735c6ca7b59c86d428e222_PATTERN = re.compile(r"/admin/API/mnt/Session/Delete/All")
    MISC_fc354ec4d361514a8e949f628f8e5f89_PATTERN = re.compile(r"/admin/API/mnt/Version")
    MISC_e346dbd9f9df554da3a3bcc06f4e77d5_PATTERN = re.compile(r"/admin/API/mnt/FailureReasons")
    MISC_8877b26746235997bc32ace7d67d6987_PATTERN = re.compile(r"/admin/API/mnt/AuthStatus/MACAddress/string/string/string/All")
    MISC_7f73477346fb5e7097d915c7f0a99659_PATTERN = re.compile(r"/admin/API/mnt/CoA/Reauth/string/string/string")
    MISC_5504a097870d5734861255a347911a24_PATTERN = re.compile(r"/admin/API/mnt/CoA/Disconnect>/string/string/string/string/{string}")
    MISC_644ab0a3ec0359faa72142f074145f6a_PATTERN = re.compile(r"/admin/API/mnt/AcctStatus/MACAddress/string/string")
    CONSUMER_91101b93b991556cae0fdd562c5e3f63_PATTERN = re.compile(r"/pxgrid/ise/radius/control/AccountCreate")
    CONSUMER_d1f92a9024975e9dad6114255be546bd_PATTERN = re.compile(r"/pxgrid/ise/radius/control/AccountActivate")
    CONSUMER_98c8ffe8c6095203a83131f49d4c8bb2_PATTERN = re.compile(r"/pxgrid/ise/radius/control/ServiceLookup")
    CONSUMER_eaad68e7996c5562901de57bf5a0420a_PATTERN = re.compile(r"/pxgrid/ise/radius/control/AccessSecret")
    MDM_3f66874f1141550da6104eff5428d37a_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/mdm/getEndpoints")
    MDM_6419150c239256209b64afc9e5522e11_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/mdm/getEndpointByMacAddress")
    MDM_0239282311e55709895e677699dfc3f7_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/mdm/getEndpointsByType")
    MDM_339bf2a72bc05f5aabd3a79a5188d86a_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/mdm/getEndpointsByOsType")
    PROFILER_dac693445cb95c6996cf6c7d85dece35_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/config/profiler/getProfiles")
    PROVIDER_61c9daa26d4b5b80a41d4b7ff9359380_PATTERN = re.compile(r"/pxgrid/ise/radius/control/ServiceRegister")
    PROVIDER_b480aaa729e75e3d872d0b30a3f8b804_PATTERN = re.compile(r"/pxgrid/ise/radius/control/ServiceUnregister")
    PROVIDER_ed4d852c55cd54c480986bec7fd9a8bb_PATTERN = re.compile(r"/pxgrid/ise/radius/control/ServiceReregister")
    PROVIDER_c9088df384b458c3991fed7f718971d5_PATTERN = re.compile(r"/pxgrid/ise/radius/control/Authorization")
    RADIUS_FAILURE_13a3d2bc1bed5e90b1056649e7703d77_PATTERN = re.compile(r"/pxgrid/ise/radius/getFailures")
    SESSION_DIRECTORY_9a86b36d56165904911f133e10d4f955_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/session/getSessions")
    SESSION_DIRECTORY_12d6da2024445b2cb8a146fe19889e71_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/session/getSessionsForRecovery")
    SESSION_DIRECTORY_2515a470322e5500949321c2cbc1b9c9_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/session/getSessionByIpAddress")
    SESSION_DIRECTORY_e564f3d00647543db29d1ca6865bc8d0_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/session/getSessionByMacAddress")
    SESSION_DIRECTORY_f8021c1d176c5de9b8b41dcde0f0268e_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/session/getUserGroups")
    SESSION_DIRECTORY_1f674031faf65cac8e2f5581bdef4788_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/session/getUserGroupByUserName")
    SYSTEM_HEALTH_0f67f5c0641d55708b20ffc56f374854_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/system/getHealths")
    SYSTEM_HEALTH_048aadb0c21d5146a207994d493fe9a5_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/system/getPerformances")
    TRUST_SEC_CONFIGURATION_9b5b0eb1671a51758acf5ec364d80738_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/config/trustsec/getSecurityGroups")
    TRUST_SEC_CONFIGURATION_02b4aa5797455ee4a27390b77262992d_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/config/trustsec/getSecurityGroupAcls")
    TRUST_SEC_CONFIGURATION_3da8b5be1a475510a5aa1593d625ffbb_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/config/trustsec/getEgressPolicies")
    TRUST_SEC_CONFIGURATION_3f9e6e1c33155fdd9a88f48d093f375b_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/config/trustsec/getEgressMatrices")
    TRUST_SEC_SXP_900a7bddaf5159e68b2caeb19b9979c4_PATTERN = re.compile(r"/pxgrid/ise/radius/ise/sxp/getBindings")
    VERSION_AND_PATCH_edea91f35e90539f87a80eb107e02fff_PATTERN = re.compile(r"/ers/config/op/systemconfig/iseversion")

    def matches_TASKS_38eb7df265a55d2cbedb08847549b39a(self):
        return re.search(
            self.TASKS_38eb7df265a55d2cbedb08847549b39a_PATTERN,
            self.path
        )

    def tasks_get_task_status_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps([{'id': 'string', 'executionStatus': 'string', 'moduleType': 'string', 'startTime': 'string', 'resourcesCount': 0, 'successCount': 0, 'failCount': 0, 'detailStatus': [{}]}])
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TASKS_bcee1c9523a45056ab79dc64bdf827fe(self):
        return re.search(
            self.TASKS_bcee1c9523a45056ab79dc64bdf827fe_PATTERN,
            self.path
        )

    def tasks_get_task_status_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string', 'executionStatus': 'string', 'moduleType': 'string', 'startTime': 'string', 'resourcesCount': 0, 'successCount': 0, 'failCount': 0, 'detailStatus': [{}]})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NODE_DEPLOYMENT_fa838e78175e51b4bcfb0821c19b81b7(self):
        return re.search(
            self.NODE_DEPLOYMENT_fa838e78175e51b4bcfb0821c19b81b7_PATTERN,
            self.path
        )

    def node_deployment_get_all_nodes_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'hostname': 'string', 'personaType': ['string'], 'roles': ['string'], 'services': ['string'], 'nodeStatus': 'string'}]})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NODE_DEPLOYMENT_e82e46732de25832a543c4640312588c(self):
        return re.search(
            self.NODE_DEPLOYMENT_e82e46732de25832a543c4640312588c_PATTERN,
            self.path
        )

    def node_deployment_register_node_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'code': 0, 'message': 'string', 'rootCause': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NODE_DEPLOYMENT_42b11e2f1af656bcb5880a7b33720ec5(self):
        return re.search(
            self.NODE_DEPLOYMENT_42b11e2f1af656bcb5880a7b33720ec5_PATTERN,
            self.path
        )

    def node_deployment_promote_node_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'code': 0, 'message': 'string', 'rootCause': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NODE_DEPLOYMENT_ae8d7c8f33bb52ceb04880845f2f45ba(self):
        return re.search(
            self.NODE_DEPLOYMENT_ae8d7c8f33bb52ceb04880845f2f45ba_PATTERN,
            self.path
        )

    def node_deployment_get_node_details_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'hostname': 'string', 'fqdn': 'string', 'ipAddress': 'string', 'nodeType': 'string', 'administration': {'isEnabled': True, 'role': 'string'}, 'generalSettings': {'monitoring': {'isEnabled': True, 'role': 'string', 'otherMonitoringNode': 'string', 'isMntDedicated': True, 'policyservice': {'enabled': True, 'sessionService': {'isEnabled': True, 'nodegroup': 'string'}, 'enableProfilingService': True, 'enableNACService': True, 'sxpservice': {'isEnabled': True, 'userInterface': 'string'}, 'enableDeviceAdminService': True, 'enablePassiveIdentityService': True}, 'enablePXGrid': True}}, 'profilingConfiguration': {'netflow': {'enabled': True, 'interface': 'string', 'port': {}, 'description': 'string'}, 'dhcp': {'enabled': True, 'interface': 'string', 'port': {}, 'description': 'string'}, 'dhcpSpan': {'enabled': True, 'interface': 'string', 'description': 'string'}, 'http': {'enabled': True, 'interface': 'string', 'description': 'string'}, 'radius': {'enabled': True, 'description': 'string'}, 'nmap': {'enabled': True, 'description': 'string'}, 'dns': {'enabled': True, 'description': 'string'}, 'snmpQuery': {'enabled': True, 'description': 'string', 'retries': 0, 'timeout': 0, 'eventTimeout': 0}, 'snmpTrap': {'linkTrapQuery': True, 'macTrapQuery': True, 'interface': 'string', 'port': {}, 'description': 'string'}, 'activeDirectory': {'enabled': True, 'daysBeforeRescan': 0, 'description': 'string'}, 'pxgrid': {'enabled': True, 'description': 'string'}}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NODE_DEPLOYMENT_682c1fa3bf115c77be99b602aca1493b(self):
        return re.search(
            self.NODE_DEPLOYMENT_682c1fa3bf115c77be99b602aca1493b_PATTERN,
            self.path
        )

    def node_deployment_update_node_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'code': 0, 'message': 'string', 'rootCause': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NODE_DEPLOYMENT_161d26670a205a78800cb50673027a6e(self):
        return re.search(
            self.NODE_DEPLOYMENT_161d26670a205a78800cb50673027a6e_PATTERN,
            self.path
        )

    def node_deployment_delete_node_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'code': 0, 'message': 'string', 'rootCause': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NODE_GROUP_a0824f9a589c58cd8df522524cb550ad(self):
        return re.search(
            self.NODE_GROUP_a0824f9a589c58cd8df522524cb550ad_PATTERN,
            self.path
        )

    def node_group_get_node_groups_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'name': 'string', 'description': 'string', 'mar-cache': {'enabled': True, 'replication-timeout': 0, 'replication-attempts': 0, 'query-timeout': 0, 'query-attempts': 0}}]})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NODE_GROUP_64a0aadd33595645bf671efc4912f89a(self):
        return re.search(
            self.NODE_GROUP_64a0aadd33595645bf671efc4912f89a_PATTERN,
            self.path
        )

    def node_group_get_node_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'name': 'string', 'description': 'string', 'mar-cache': {'enabled': True, 'replication-timeout': 0, 'replication-attempts': 0, 'query-timeout': 0, 'query-attempts': 0}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NODE_GROUP_f41d844dbee15f7680920652004f69b6(self):
        return re.search(
            self.NODE_GROUP_f41d844dbee15f7680920652004f69b6_PATTERN,
            self.path
        )

    def node_group_create_node_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'code': 0, 'message': 'string', 'rootCause': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NODE_GROUP_2875a99695fd5ee0b00efce79a5761ff(self):
        return re.search(
            self.NODE_GROUP_2875a99695fd5ee0b00efce79a5761ff_PATTERN,
            self.path
        )

    def node_group_update_node_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'code': 0, 'message': 'string', 'rootCause': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NODE_GROUP_2c5c37c343c050e0af67b2223e64faf3(self):
        return re.search(
            self.NODE_GROUP_2c5c37c343c050e0af67b2223e64faf3_PATTERN,
            self.path
        )

    def node_group_delete_node_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'code': 0, 'message': 'string', 'rootCause': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PAN_HA_02daa171ab765a02a714c48376b3790d(self):
        return re.search(
            self.PAN_HA_02daa171ab765a02a714c48376b3790d_PATTERN,
            self.path
        )

    def pan_ha_get_pan_ha_status_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'isEnabled': True, 'primaryHealthCheckNode': 'string', 'secondaryHealthCheckNode': 'string', 'pollingInterval': 0, 'failedAttempts': 0}]})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PAN_HA_fc9a4ee495785518bd2251b6b4fb41f4(self):
        return re.search(
            self.PAN_HA_fc9a4ee495785518bd2251b6b4fb41f4_PATTERN,
            self.path
        )

    def pan_ha_enable_pan_ha_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'code': 0, 'message': 'string', 'rootCause': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PAN_HA_a1e3cde0c3f254b39caaaf7c907ae67e(self):
        return re.search(
            self.PAN_HA_a1e3cde0c3f254b39caaaf7c907ae67e_PATTERN,
            self.path
        )

    def pan_ha_disable_pan_ha_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'code': 0, 'message': 'string', 'rootCause': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_REPLICATION_STATUS_7ae615b5e28c54639f44bd10e5b36601(self):
        return re.search(
            self.REPLICATION_STATUS_7ae615b5e28c54639f44bd10e5b36601_PATTERN,
            self.path
        )

    def replication_status_get_node_replication_status_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'NodeStatus': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SYNC_ISE_NODE_582ad69fa1d850f4993bbfc888749fa0(self):
        return re.search(
            self.SYNC_ISE_NODE_582ad69fa1d850f4993bbfc888749fa0_PATTERN,
            self.path
        )

    def sync_ise_node_sync_node_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'code': 0, 'message': 'string', 'rootCause': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_BACKUP_AND_RESTORE_b9638a67f60d5a6aa476af13632d96bd(self):
        return re.search(
            self.BACKUP_AND_RESTORE_b9638a67f60d5a6aa476af13632d96bd_PATTERN,
            self.path
        )

    def backup_and_restore_config_backup_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'id': 'string', 'message': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_BACKUP_AND_RESTORE_39527e9813ff50a9bcbbd5d539ed19d8(self):
        return re.search(
            self.BACKUP_AND_RESTORE_39527e9813ff50a9bcbbd5d539ed19d8_PATTERN,
            self.path
        )

    def backup_and_restore_cancel_backup_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'action': 'string', 'details': 'string', 'error': 'string', 'hostName': 'string', 'initiatedFrom': 'string', 'justComplete': 'string', 'message': 'string', 'name': 'string', 'percentComplete': 'string', 'repository': 'string', 'scheduled': 'string', 'startDate': 'string', 'status': 'string', 'type': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_BACKUP_AND_RESTORE_b0b71a5f25825202b6cb339ce1a5a8d4(self):
        return re.search(
            self.BACKUP_AND_RESTORE_b0b71a5f25825202b6cb339ce1a5a8d4_PATTERN,
            self.path
        )

    def backup_and_restore_get_last_config_backup_status_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'action': 'string', 'details': 'string', 'error': 'string', 'hostName': 'string', 'initiatedFrom': 'string', 'justComplete': 'string', 'message': 'string', 'name': 'string', 'percentComplete': 'string', 'repository': 'string', 'scheduled': 'string', 'startDate': 'string', 'status': 'string', 'type': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_BACKUP_AND_RESTORE_db3505847b4e5f37a5c74bc41df54be3(self):
        return re.search(
            self.BACKUP_AND_RESTORE_db3505847b4e5f37a5c74bc41df54be3_PATTERN,
            self.path
        )

    def backup_and_restore_restore_config_backup_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'id': 'string', 'message': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_BACKUP_AND_RESTORE_5329d31fa60f5575a2ed23cee473c0fc(self):
        return re.search(
            self.BACKUP_AND_RESTORE_5329d31fa60f5575a2ed23cee473c0fc_PATTERN,
            self.path
        )

    def backup_and_restore_update_scheduled_config_backup_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'message': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_BACKUP_AND_RESTORE_dd4581dd32f65e8c83cca2f0a97af3e2(self):
        return re.search(
            self.BACKUP_AND_RESTORE_dd4581dd32f65e8c83cca2f0a97af3e2_PATTERN,
            self.path
        )

    def backup_and_restore_create_scheduled_config_backup_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'message': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_REPOSITORY_a83213678e6b58528986f1219d9f12ce(self):
        return re.search(
            self.REPOSITORY_a83213678e6b58528986f1219d9f12ce_PATTERN,
            self.path
        )

    def repository_get_repositories_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'name': 'string', 'protocol': 'string', 'path': 'string', 'password': 'string', 'serverName': 'string', 'userName': 'string', 'enablePki': True}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_REPOSITORY_17edcb0e8c6b54709d4d61ea23b45f84(self):
        return re.search(
            self.REPOSITORY_17edcb0e8c6b54709d4d61ea23b45f84_PATTERN,
            self.path
        )

    def repository_create_repository_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'success': {'message': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_REPOSITORY_8a79dc5595ac51d1970b8d53498d3c32(self):
        return re.search(
            self.REPOSITORY_8a79dc5595ac51d1970b8d53498d3c32_PATTERN,
            self.path
        )

    def repository_get_repository_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'name': 'string', 'protocol': 'string', 'path': 'string', 'password': 'string', 'serverName': 'string', 'userName': 'string', 'enablePki': True}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_REPOSITORY_62488ad8eb56595e86c4300607ec4dd3(self):
        return re.search(
            self.REPOSITORY_62488ad8eb56595e86c4300607ec4dd3_PATTERN,
            self.path
        )

    def repository_update_repository_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'success': {'message': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_REPOSITORY_d3b49f09d7f954bdb6f413e1785a05d7(self):
        return re.search(
            self.REPOSITORY_d3b49f09d7f954bdb6f413e1785a05d7_PATTERN,
            self.path
        )

    def repository_delete_repository_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'success': {'message': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_REPOSITORY_fc645a4297f55557af8d398f07f6d0a0(self):
        return re.search(
            self.REPOSITORY_fc645a4297f55557af8d398f07f6d0a0_PATTERN,
            self.path
        )

    def repository_get_repository_files_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': ['string'], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ANC_ENDPOINT_5ffbc09a97795b8d872a943895c00345(self):
        return re.search(
            self.ANC_ENDPOINT_5ffbc09a97795b8d872a943895c00345_PATTERN,
            self.path
        )

    def anc_endpoint_get_anc_endpoint_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ErsAncEndpoint': {'id': 'string', 'macAddress': 'string', 'policyName': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ANC_ENDPOINT_2131fc6670fd50dfb04b1f6b16981256(self):
        return re.search(
            self.ANC_ENDPOINT_2131fc6670fd50dfb04b1f6b16981256_PATTERN,
            self.path
        )

    def anc_endpoint_clear_anc_endpoint_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ANC_ENDPOINT_502e681462295b8b8faea9ce6099ff0c(self):
        return re.search(
            self.ANC_ENDPOINT_502e681462295b8b8faea9ce6099ff0c_PATTERN,
            self.path
        )

    def anc_endpoint_get_all_anc_endpoint_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ANC_ENDPOINT_136bc936bcb25464b9f3f227647b0443(self):
        return re.search(
            self.ANC_ENDPOINT_136bc936bcb25464b9f3f227647b0443_PATTERN,
            self.path
        )

    def anc_endpoint_apply_anc_endpoint_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ANC_ENDPOINT_d5eb6cea45635ef58f5bc624de004f16(self):
        return re.search(
            self.ANC_ENDPOINT_d5eb6cea45635ef58f5bc624de004f16_PATTERN,
            self.path
        )

    def anc_endpoint_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ANC_ENDPOINT_5e6167fc5cb6593b8b48429187a26a67(self):
        return re.search(
            self.ANC_ENDPOINT_5e6167fc5cb6593b8b48429187a26a67_PATTERN,
            self.path
        )

    def anc_endpoint_bulk_request_for_anc_endpoint_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ANC_ENDPOINT_0a1c6b9323e55505830673a1819840f3(self):
        return re.search(
            self.ANC_ENDPOINT_0a1c6b9323e55505830673a1819840f3_PATTERN,
            self.path
        )

    def anc_endpoint_monitor_bulk_status_anc_endpoint_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'BulkStatus': {'bulkID': 'string', 'executionStatus': 'string', 'operationType': 'string', 'startTime': 'string', 'resourcesCount': 0, 'successCount': 0, 'failCount': 0, 'resourcesStatus': [{'id': 'string', 'name': 'string', 'description': 'string', 'resourceExecutionStatus': 'string', 'status': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ANC_POLICY_983a095b061f564ebba331f66505b0e3(self):
        return re.search(
            self.ANC_POLICY_983a095b061f564ebba331f66505b0e3_PATTERN,
            self.path
        )

    def anc_policy_get_anc_policy_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ErsAncPolicy': {'id': 'string', 'name': 'string', 'action': ['string'], 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ANC_POLICY_f41f77362663580d8cc3e6e88623889d(self):
        return re.search(
            self.ANC_POLICY_f41f77362663580d8cc3e6e88623889d_PATTERN,
            self.path
        )

    def anc_policy_get_anc_policy_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ErsAncPolicy': {'id': 'string', 'name': 'string', 'action': ['string'], 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ANC_POLICY_1d79b507bda155c180d42f0a67ef64d5(self):
        return re.search(
            self.ANC_POLICY_1d79b507bda155c180d42f0a67ef64d5_PATTERN,
            self.path
        )

    def anc_policy_update_anc_policy_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': [{'field': 'string', 'oldValue': 'string', 'newValue': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ANC_POLICY_7c6b8dd764e052699d4d7a0d8ba43640(self):
        return re.search(
            self.ANC_POLICY_7c6b8dd764e052699d4d7a0d8ba43640_PATTERN,
            self.path
        )

    def anc_policy_delete_anc_policy_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ANC_POLICY_440813c9722c56108cac8ca50bf8f01c(self):
        return re.search(
            self.ANC_POLICY_440813c9722c56108cac8ca50bf8f01c_PATTERN,
            self.path
        )

    def anc_policy_get_all_anc_policy_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ANC_POLICY_2acfdb4060de5a1895b383238c205986(self):
        return re.search(
            self.ANC_POLICY_2acfdb4060de5a1895b383238c205986_PATTERN,
            self.path
        )

    def anc_policy_create_anc_policy_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ANC_POLICY_b01a12e2b55e582084fab915465bf962(self):
        return re.search(
            self.ANC_POLICY_b01a12e2b55e582084fab915465bf962_PATTERN,
            self.path
        )

    def anc_policy_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ANC_POLICY_4d67f9f6fba65dcbbcf64ca3e31b39a6(self):
        return re.search(
            self.ANC_POLICY_4d67f9f6fba65dcbbcf64ca3e31b39a6_PATTERN,
            self.path
        )

    def anc_policy_bulk_request_for_anc_policy_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ANC_POLICY_10023cdff02b5185b9b54c9e58762704(self):
        return re.search(
            self.ANC_POLICY_10023cdff02b5185b9b54c9e58762704_PATTERN,
            self.path
        )

    def anc_policy_monitor_bulk_status_anc_policy_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'BulkStatus': {'bulkID': 'string', 'executionStatus': 'string', 'operationType': 'string', 'startTime': 'string', 'resourcesCount': 0, 'successCount': 0, 'failCount': 0, 'resourcesStatus': [{'id': 'string', 'name': 'string', 'description': 'string', 'resourceExecutionStatus': 'string', 'status': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CLEAR_THREATS_AND_VULNERABILITIES_e3110fc63ecb5428a075a8af8497fb35(self):
        return re.search(
            self.CLEAR_THREATS_AND_VULNERABILITIES_e3110fc63ecb5428a075a8af8497fb35_PATTERN,
            self.path
        )

    def clear_threats_and_vulnerabilities_clear_threats_and_vulnerabilities_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CLEAR_THREATS_AND_VULNERABILITIES_83379c74d24e5ae9bb90f798a190cca3(self):
        return re.search(
            self.CLEAR_THREATS_AND_VULNERABILITIES_83379c74d24e5ae9bb90f798a190cca3_PATTERN,
            self.path
        )

    def clear_threats_and_vulnerabilities_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NODE_DETAILS_ab48268c76aa598788a5ebc370226f3a(self):
        return re.search(
            self.NODE_DETAILS_ab48268c76aa598788a5ebc370226f3a_PATTERN,
            self.path
        )

    def node_details_get_node_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'Node': {'id': 'string', 'name': 'string', 'gateWay': 'string', 'userName': 'string', 'passWord': 'string', 'displayName': 'string', 'inDeployment': True, 'otherPapFqdn': 'string', 'ipAddresses': ['string'], 'ipAddress': 'string', 'sxpIpAddress': 'string', 'nodeServiceTypes': 'string', 'fqdn': 'string', 'papNode': True, 'primaryPapNode': True, 'pxGridNode': True, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NODE_DETAILS_0397bb2e9d6651c7bf18c1b60ff7eb14(self):
        return re.search(
            self.NODE_DETAILS_0397bb2e9d6651c7bf18c1b60ff7eb14_PATTERN,
            self.path
        )

    def node_details_get_node_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'Node': {'id': 'string', 'name': 'string', 'gateWay': 'string', 'userName': 'string', 'passWord': 'string', 'displayName': 'string', 'inDeployment': True, 'otherPapFqdn': 'string', 'ipAddresses': ['string'], 'ipAddress': 'string', 'sxpIpAddress': 'string', 'nodeServiceTypes': 'string', 'fqdn': 'string', 'papNode': True, 'primaryPapNode': True, 'pxGridNode': True, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NODE_DETAILS_775d9b8599f55fc4a1bd9d6ac02619eb(self):
        return re.search(
            self.NODE_DETAILS_775d9b8599f55fc4a1bd9d6ac02619eb_PATTERN,
            self.path
        )

    def node_details_get_all_nodes_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NODE_DETAILS_ca9a3d8217d5507aa11020bee82ef228(self):
        return re.search(
            self.NODE_DETAILS_ca9a3d8217d5507aa11020bee82ef228_PATTERN,
            self.path
        )

    def node_details_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PSN_NODE_DETAILS_WITH_RADIUS_SERVICE_ab225d0b2a6c52a99df1f1d8fb6a4dac(self):
        return re.search(
            self.PSN_NODE_DETAILS_WITH_RADIUS_SERVICE_ab225d0b2a6c52a99df1f1d8fb6a4dac_PATTERN,
            self.path
        )

    def psn_node_details_with_radius_service_get_session_service_node_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SessionServiceNode': {'id': 'string', 'name': 'string', 'description': 'string', 'ipAddress': 'string', 'gateWay': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PSN_NODE_DETAILS_WITH_RADIUS_SERVICE_c988bb742d055294b74b4d6916ca1ada(self):
        return re.search(
            self.PSN_NODE_DETAILS_WITH_RADIUS_SERVICE_c988bb742d055294b74b4d6916ca1ada_PATTERN,
            self.path
        )

    def psn_node_details_with_radius_service_get_session_service_node_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SessionServiceNode': {'id': 'string', 'name': 'string', 'description': 'string', 'ipAddress': 'string', 'gateWay': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PSN_NODE_DETAILS_WITH_RADIUS_SERVICE_66dccbf248575cbeb3cd3dda5cdbcf20(self):
        return re.search(
            self.PSN_NODE_DETAILS_WITH_RADIUS_SERVICE_66dccbf248575cbeb3cd3dda5cdbcf20_PATTERN,
            self.path
        )

    def psn_node_details_with_radius_service_get_all_session_service_node_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PSN_NODE_DETAILS_WITH_RADIUS_SERVICE_05c0bfee23f95034842993a83d77c4e4(self):
        return re.search(
            self.PSN_NODE_DETAILS_WITH_RADIUS_SERVICE_05c0bfee23f95034842993a83d77c4e4_PATTERN,
            self.path
        )

    def psn_node_details_with_radius_service_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PULL_DEPLOYMENT_INFO_f9159c9f9a1951568daee7080e1dda47(self):
        return re.search(
            self.PULL_DEPLOYMENT_INFO_f9159c9f9a1951568daee7080e1dda47_PATTERN,
            self.path
        )

    def pull_deployment_info_get_all_deployment_info_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSDeploymentInfo': {'networkAccessInfo': {'deploymentID': 'string', 'isCsnEnabled': True, 'nodeList': {'nodeAndScope': [{}]}, 'sdaVNs': [], 'trustSecControl': 'string', 'radius3RdParty': []}, 'profilerInfo': {'deploymentID': 'string', 'nodeList': {'node': [{'onlineSubscriptionEnabled': True, 'lastAppliedFeedDateTime': 'string', 'scope': 'string', 'profiles': [{'profile': [], 'customProfilesCount': 0, 'endpointTypes': 'string', 'totalProfilesCount': 0, 'uniqueEndpointsCount': 0, 'unknownEndpointsCount': 0, 'totalEndpointsCount': 0, 'unknownEndpointsPercentage': 0}]}]}}, 'deploymentInfo': {'deploymentID': 'string', 'versionHistoryInfo': [{'opType': 'string', 'mainVersion': 'string', 'epochTime': 0}], 'nodeList': {'nodeAndNodeCountAndCountInfo': [{'name': 'string', 'value': 'string', 'declaredType': 'string', 'scope': 'string', 'nil': True, 'globalScope': True, 'typeSubstituted': True}]}, 'fipsstatus': 'string'}, 'nadInfo': {'nodeList': {'nodeAndScope': [{}]}, 'nadcountInfo': {'totalActiveNADCount': 0}}, 'mdmInfo': {'activeMdmServersCount': 0, 'activeDesktopMdmServersCount': 0, 'activeMobileMdmServersCount': 0, 'deploymentID': 'string', 'nodeList': {'nodeAndScope': [{}]}}, 'licensesInfo': {'deploymentID': 'string', 'nodeList': {'node': [{}]}}, 'postureInfo': {'content': [{'name': 'string', 'value': 'string', 'declaredType': 'string', 'scope': 'string', 'nil': True, 'globalScope': True, 'typeSubstituted': True}]}, 'kongInfo': {'deploymentID': 'string', 'nodeList': {'node': [{'sn': 'string', 'service': [{'serviceName': 'string', 'route': [{'routeName': 'string', 'httpCount': {}, 'latencyCount': {}, 'latencySum': {}}]}]}]}}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PULL_DEPLOYMENT_INFO_8698cc09209259dcbde7c851b5a6eda6(self):
        return re.search(
            self.PULL_DEPLOYMENT_INFO_8698cc09209259dcbde7c851b5a6eda6_PATTERN,
            self.path
        )

    def pull_deployment_info_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PX_GRID_NODE_a2a7f23f85105113954c87a917b7455f(self):
        return re.search(
            self.PX_GRID_NODE_a2a7f23f85105113954c87a917b7455f_PATTERN,
            self.path
        )

    def px_grid_node_approve_px_grid_node_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PX_GRID_NODE_111a9d109aac585a89bdd3fae400064b(self):
        return re.search(
            self.PX_GRID_NODE_111a9d109aac585a89bdd3fae400064b_PATTERN,
            self.path
        )

    def px_grid_node_get_px_grid_node_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'PxgridNode': {'id': 'string', 'name': 'string', 'description': 'string', 'status': 'string', 'authMethod': 'string', 'groups': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PX_GRID_NODE_849e718d5054593b94a2fef39461c24a(self):
        return re.search(
            self.PX_GRID_NODE_849e718d5054593b94a2fef39461c24a_PATTERN,
            self.path
        )

    def px_grid_node_delete_px_grid_node_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PX_GRID_NODE_d24ade0b53405fbc898cb0cc1ea57fb8(self):
        return re.search(
            self.PX_GRID_NODE_d24ade0b53405fbc898cb0cc1ea57fb8_PATTERN,
            self.path
        )

    def px_grid_node_get_px_grid_node_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'PxgridNode': {'id': 'string', 'name': 'string', 'description': 'string', 'status': 'string', 'authMethod': 'string', 'groups': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PX_GRID_NODE_52661028d97156379640002f79b2007c(self):
        return re.search(
            self.PX_GRID_NODE_52661028d97156379640002f79b2007c_PATTERN,
            self.path
        )

    def px_grid_node_get_all_px_grid_node_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PX_GRID_NODE_73c2962d70ef5964be55cfeae68e5ba6(self):
        return re.search(
            self.PX_GRID_NODE_73c2962d70ef5964be55cfeae68e5ba6_PATTERN,
            self.path
        )

    def px_grid_node_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SUPPORT_BUNDLE_DOWNLOAD_737531846d125b968b9d362a3458621d(self):
        return re.search(
            self.SUPPORT_BUNDLE_DOWNLOAD_737531846d125b968b9d362a3458621d_PATTERN,
            self.path
        )

    def support_bundle_download_download_support_bundle_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SUPPORT_BUNDLE_DOWNLOAD_25c57752629f546fb86e84c59285350f(self):
        return re.search(
            self.SUPPORT_BUNDLE_DOWNLOAD_25c57752629f546fb86e84c59285350f_PATTERN,
            self.path
        )

    def support_bundle_download_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SUPPORT_BUNDLE_STATUS_cec7dc317e875ff0a315a7c0556f9c51(self):
        return re.search(
            self.SUPPORT_BUNDLE_STATUS_cec7dc317e875ff0a315a7c0556f9c51_PATTERN,
            self.path
        )

    def support_bundle_status_get_support_bundle_status_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SBStatus': {'id': 'string', 'name': 'string', 'description': 'string', 'fileName': 'string', 'fileSize': 'string', 'hostName': 'string', 'message': 'string', 'startTime': 'string', 'status': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SUPPORT_BUNDLE_STATUS_505300e162f051d58c6ae9d5e3851780(self):
        return re.search(
            self.SUPPORT_BUNDLE_STATUS_505300e162f051d58c6ae9d5e3851780_PATTERN,
            self.path
        )

    def support_bundle_status_get_all_support_bundle_status_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SUPPORT_BUNDLE_STATUS_7ae30c71acc45385a6b3e9a49a8281a9(self):
        return re.search(
            self.SUPPORT_BUNDLE_STATUS_7ae30c71acc45385a6b3e9a49a8281a9_PATTERN,
            self.path
        )

    def support_bundle_status_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SUPPORT_BUNDLE_TRIGGER_CONFIGURATION_492171fac48e5c63abfe2feec6fd1903(self):
        return re.search(
            self.SUPPORT_BUNDLE_TRIGGER_CONFIGURATION_492171fac48e5c63abfe2feec6fd1903_PATTERN,
            self.path
        )

    def support_bundle_trigger_configuration_create_support_bundle_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SUPPORT_BUNDLE_TRIGGER_CONFIGURATION_a2b17c3c4eab52caa2fc7c811965c79d(self):
        return re.search(
            self.SUPPORT_BUNDLE_TRIGGER_CONFIGURATION_a2b17c3c4eab52caa2fc7c811965c79d_PATTERN,
            self.path
        )

    def support_bundle_trigger_configuration_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_87efa004c89a5b85ad30e0dde622bfaf(self):
        return re.search(
            self.CERTIFICATES_87efa004c89a5b85ad30e0dde622bfaf_PATTERN,
            self.path
        )

    def certificates_get_csrs_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'friendlyName': 'string', 'groupTag': 'string', 'hostName': 'string', 'id': 'string', 'keySize': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'signatureAlgorithm': 'string', 'subject': 'string', 'timeStamp': 'string', 'usedFor': 'string'}], 'nextPage': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'previousPage': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_dd7a13ef2dea5b9fa6c4d67839133bbf(self):
        return re.search(
            self.CERTIFICATES_dd7a13ef2dea5b9fa6c4d67839133bbf_PATTERN,
            self.path
        )

    def certificates_generate_csr_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'message': 'string'}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_0910f99dc34755cf954945d5575e3072(self):
        return re.search(
            self.CERTIFICATES_0910f99dc34755cf954945d5575e3072_PATTERN,
            self.path
        )

    def certificates_export_csr_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps('string')
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_db47e53374a85830af220e5f982d10da(self):
        return re.search(
            self.CERTIFICATES_db47e53374a85830af220e5f982d10da_PATTERN,
            self.path
        )

    def certificates_generate_intermediate_ca_csr_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'message': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_5015d080d7635e27aef80f42d20b01c8(self):
        return re.search(
            self.CERTIFICATES_5015d080d7635e27aef80f42d20b01c8_PATTERN,
            self.path
        )

    def certificates_get_csr_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_dde06bf20b6b5f71b8f0782f3750c242(self):
        return re.search(
            self.CERTIFICATES_dde06bf20b6b5f71b8f0782f3750c242_PATTERN,
            self.path
        )

    def certificates_delete_csr_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'message': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_7222975970e85c38bcad4249948c550b(self):
        return re.search(
            self.CERTIFICATES_7222975970e85c38bcad4249948c550b_PATTERN,
            self.path
        )

    def certificates_regenerate_ise_root_ca_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'message': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_ce788c3408de5056a2e71955f86d6f05(self):
        return re.search(
            self.CERTIFICATES_ce788c3408de5056a2e71955f86d6f05_PATTERN,
            self.path
        )

    def certificates_renew_certs_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'message': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_77c39f0f97cb53e19a03f2ea53f5b831(self):
        return re.search(
            self.CERTIFICATES_77c39f0f97cb53e19a03f2ea53f5b831_PATTERN,
            self.path
        )

    def certificates_bind_csr_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'message': 'string', 'status': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_da5ac537bf475538b7bc42c8cce2e530(self):
        return re.search(
            self.CERTIFICATES_da5ac537bf475538b7bc42c8cce2e530_PATTERN,
            self.path
        )

    def certificates_export_system_cert_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps('string')
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_adde5bf7c9185218b955ff0c365fcc4c(self):
        return re.search(
            self.CERTIFICATES_adde5bf7c9185218b955ff0c365fcc4c_PATTERN,
            self.path
        )

    def certificates_import_system_cert_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'id': 'string', 'message': 'string', 'status': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_c2e43687a3205903a3f60728b87f1865(self):
        return re.search(
            self.CERTIFICATES_c2e43687a3205903a3f60728b87f1865_PATTERN,
            self.path
        )

    def certificates_get_system_certificates_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'expirationDate': 'string', 'friendlyName': 'string', 'groupTag': 'string', 'id': 'string', 'issuedBy': 'string', 'issuedTo': 'string', 'keySize': 0, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'portalsUsingTheTag': 'string', 'selfSigned': True, 'serialNumberDecimalFormat': 'string', 'sha256Fingerprint': 'string', 'signatureAlgorithm': 'string', 'usedBy': 'string', 'validFrom': 'string'}], 'nextPage': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'previousPage': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_c4e07bc79feb5e19bf6cc60220f47bdf(self):
        return re.search(
            self.CERTIFICATES_c4e07bc79feb5e19bf6cc60220f47bdf_PATTERN,
            self.path
        )

    def certificates_get_system_certificate_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'expirationDate': 'string', 'friendlyName': 'string', 'groupTag': 'string', 'id': 'string', 'issuedBy': 'string', 'issuedTo': 'string', 'keySize': 0, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'portalsUsingTheTag': 'string', 'selfSigned': True, 'serialNumberDecimalFormat': 'string', 'sha256Fingerprint': 'string', 'signatureAlgorithm': 'string', 'usedBy': 'string', 'validFrom': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_e9594a91bd735eaabe2eb50038e9d05a(self):
        return re.search(
            self.CERTIFICATES_e9594a91bd735eaabe2eb50038e9d05a_PATTERN,
            self.path
        )

    def certificates_update_system_cert_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'message': 'string', 'status': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_5c55df3640a55c48bece27159ce199f8(self):
        return re.search(
            self.CERTIFICATES_5c55df3640a55c48bece27159ce199f8_PATTERN,
            self.path
        )

    def certificates_delete_system_certificate_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'message': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_df7d8ed3e15a5d1587cdd7652efe0104(self):
        return re.search(
            self.CERTIFICATES_df7d8ed3e15a5d1587cdd7652efe0104_PATTERN,
            self.path
        )

    def certificates_get_trusted_certificates_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'authenticateBeforeCRLReceived': 'string', 'automaticCRLUpdate': 'string', 'automaticCRLUpdatePeriod': 'string', 'automaticCRLUpdateUnits': 'string', 'crlDistributionUrl': 'string', 'crlDownloadFailureRetries': 'string', 'crlDownloadFailureRetriesUnits': 'string', 'description': 'string', 'downloadCRL': 'string', 'enableOCSPValidation': 'string', 'enableServerIdentityCheck': 'string', 'expirationDate': 'string', 'friendlyName': 'string', 'id': 'string', 'ignoreCRLExpiration': 'string', 'internalCA': True, 'isReferredInPolicy': True, 'issuedBy': 'string', 'issuedTo': 'string', 'keySize': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'nonAutomaticCRLUpdatePeriod': 'string', 'nonAutomaticCRLUpdateUnits': 'string', 'rejectIfNoStatusFromOCSP': 'string', 'rejectIfUnreachableFromOCSP': 'string', 'selectedOCSPService': 'string', 'serialNumberDecimalFormat': 'string', 'sha256Fingerprint': 'string', 'signatureAlgorithm': 'string', 'status': 'string', 'subject': 'string', 'trustedFor': 'string', 'validFrom': 'string'}], 'nextPage': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'previousPage': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_5978827945b45792ab0b40c8a2d3392c(self):
        return re.search(
            self.CERTIFICATES_5978827945b45792ab0b40c8a2d3392c_PATTERN,
            self.path
        )

    def certificates_export_trusted_cert_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps('string')
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_f385b6330ef6500cb599f55407695a3e(self):
        return re.search(
            self.CERTIFICATES_f385b6330ef6500cb599f55407695a3e_PATTERN,
            self.path
        )

    def certificates_import_trust_cert_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'id': 'string', 'message': 'string', 'status': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_bee89e08a5145417989aaf187a6d7b2b(self):
        return re.search(
            self.CERTIFICATES_bee89e08a5145417989aaf187a6d7b2b_PATTERN,
            self.path
        )

    def certificates_get_trusted_certificate_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'authenticateBeforeCRLReceived': 'string', 'automaticCRLUpdate': 'string', 'automaticCRLUpdatePeriod': 'string', 'automaticCRLUpdateUnits': 'string', 'crlDistributionUrl': 'string', 'crlDownloadFailureRetries': 'string', 'crlDownloadFailureRetriesUnits': 'string', 'description': 'string', 'downloadCRL': 'string', 'enableOCSPValidation': 'string', 'enableServerIdentityCheck': 'string', 'expirationDate': 'string', 'friendlyName': 'string', 'id': 'string', 'ignoreCRLExpiration': 'string', 'internalCA': True, 'isReferredInPolicy': True, 'issuedBy': 'string', 'issuedTo': 'string', 'keySize': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'nonAutomaticCRLUpdatePeriod': 'string', 'nonAutomaticCRLUpdateUnits': 'string', 'rejectIfNoStatusFromOCSP': 'string', 'rejectIfUnreachableFromOCSP': 'string', 'selectedOCSPService': 'string', 'serialNumberDecimalFormat': 'string', 'sha256Fingerprint': 'string', 'signatureAlgorithm': 'string', 'status': 'string', 'subject': 'string', 'trustedFor': 'string', 'validFrom': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_ed4e0ba952525984acfe4a151689c2eb(self):
        return re.search(
            self.CERTIFICATES_ed4e0ba952525984acfe4a151689c2eb_PATTERN,
            self.path
        )

    def certificates_update_trusted_certificate_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'message': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATES_de9ebc73cfce5059a702076cf6a0aec2(self):
        return re.search(
            self.CERTIFICATES_de9ebc73cfce5059a702076cf6a0aec2_PATTERN,
            self.path
        )

    def certificates_delete_trusted_certificate_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'message': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_e8bd869250105a2ba30dd2cb65b0b3f2(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_e8bd869250105a2ba30dd2cb65b0b3f2_PATTERN,
            self.path
        )

    def device_administration_authentication_rules_get_device_admin_policy_by_id_authentication_rule_list_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'identitySourceName': 'string', 'ifAuthFail': 'string', 'ifProcessFail': 'string', 'ifUserNotFound': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_73164e92c5af5344b4d9fdc45a282ce5(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_73164e92c5af5344b4d9fdc45a282ce5_PATTERN,
            self.path
        )

    def device_administration_authentication_rules_create_device_admin_policy_by_id_authentication_rule_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'identitySourceName': 'string', 'ifAuthFail': 'string', 'ifProcessFail': 'string', 'ifUserNotFound': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_573a1a3596305814bab0a6d05cf86280(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_573a1a3596305814bab0a6d05cf86280_PATTERN,
            self.path
        )

    def device_administration_authentication_rules_reset_hit_counts_device_admin_policy_by_id_authentication_rules_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'message': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_87d71c8af3b55abb8e5959965baf2043(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_87d71c8af3b55abb8e5959965baf2043_PATTERN,
            self.path
        )

    def device_administration_authentication_rules_get_device_admin_policy_by_id_authentication_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'identitySourceName': 'string', 'ifAuthFail': 'string', 'ifProcessFail': 'string', 'ifUserNotFound': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_7dc678d472905ab5bce9f4cba7cd7004(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_7dc678d472905ab5bce9f4cba7cd7004_PATTERN,
            self.path
        )

    def device_administration_authentication_rules_update_device_admin_policy_by_id_authentication_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'identitySourceName': 'string', 'ifAuthFail': 'string', 'ifProcessFail': 'string', 'ifUserNotFound': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_a0a005e87c6755e0bf5d4454a98f08c5(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_a0a005e87c6755e0bf5d4454a98f08c5_PATTERN,
            self.path
        )

    def device_administration_authentication_rules_delete_device_admin_policy_by_id_authentication_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_0eb446266e3d54f4a657050d4f9b0bf9(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_0eb446266e3d54f4a657050d4f9b0bf9_PATTERN,
            self.path
        )

    def device_administration_authorization_exception_rules_get_device_admin_policy_by_id_local_exception_rule_list_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'commands': ['string'], 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': 'string', 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_c730e85640aa5a59bc0e0fd95dacf889(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_c730e85640aa5a59bc0e0fd95dacf889_PATTERN,
            self.path
        )

    def device_administration_authorization_exception_rules_create_device_admin_policy_by_id_local_exception_rule_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'commands': ['string'], 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': 'string', 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_2dde23cf27e65a60a949d8f1f599b3d2(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_2dde23cf27e65a60a949d8f1f599b3d2_PATTERN,
            self.path
        )

    def device_administration_authorization_exception_rules_reset_hit_counts_device_admin_policy_by_id_local_exceptions_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'message': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_5afaa335e2545c6f8f5530cd5686366a(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_5afaa335e2545c6f8f5530cd5686366a_PATTERN,
            self.path
        )

    def device_administration_authorization_exception_rules_get_device_admin_policy_by_id_local_exception_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'commands': ['string'], 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': 'string', 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_e326f7a61069587f9a27e69433229cc7(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_e326f7a61069587f9a27e69433229cc7_PATTERN,
            self.path
        )

    def device_administration_authorization_exception_rules_update_device_admin_policy_by_id_local_exception_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'commands': ['string'], 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': 'string', 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_7c12c4eb2a5650c2b6e26a84131ef65b(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_7c12c4eb2a5650c2b6e26a84131ef65b_PATTERN,
            self.path
        )

    def device_administration_authorization_exception_rules_delete_device_admin_policy_by_id_local_exception_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_d407475db88f596390eab0a3e8c1d162(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_d407475db88f596390eab0a3e8c1d162_PATTERN,
            self.path
        )

    def device_administration_authorization_global_exception_rules_get_device_admin_policy_set_global_exception_rule_list_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'commands': ['string'], 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': 'string', 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_8558ade26d445251a45cc753f68d21bc(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_8558ade26d445251a45cc753f68d21bc_PATTERN,
            self.path
        )

    def device_administration_authorization_global_exception_rules_create_device_admin_policy_set_global_exception_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'commands': ['string'], 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': 'string', 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_6b273ca0ffac58c3921f658152c03dbb(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_6b273ca0ffac58c3921f658152c03dbb_PATTERN,
            self.path
        )

    def device_administration_authorization_global_exception_rules_reset_hit_counts_device_admin_global_exceptions_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'message': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_3a3d7e48a50d58a8a5d5720f9d55cf45(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_3a3d7e48a50d58a8a5d5720f9d55cf45_PATTERN,
            self.path
        )

    def device_administration_authorization_global_exception_rules_get_device_admin_policy_set_global_exception_by_rule_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'commands': ['string'], 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': 'string', 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_28042265da96552991705623287a164c(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_28042265da96552991705623287a164c_PATTERN,
            self.path
        )

    def device_administration_authorization_global_exception_rules_put_device_admin_policy_set_global_exception_by_rule_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'commands': ['string'], 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': 'string', 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_10281a20040d51a1ba61f4d210195e59(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_10281a20040d51a1ba61f4d210195e59_PATTERN,
            self.path
        )

    def device_administration_authorization_global_exception_rules_delete_device_admin_policyset_global_exception_by_rule_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_4e4ac2543c3b53b5982168169f0b29b4(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_4e4ac2543c3b53b5982168169f0b29b4_PATTERN,
            self.path
        )

    def device_administration_authorization_rules_get_device_admin_policy_by_id_authorization_rule_list_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'commands': ['string'], 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': 'string', 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_8440a5fd2b5d5306b9941387f400c7a0(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_8440a5fd2b5d5306b9941387f400c7a0_PATTERN,
            self.path
        )

    def device_administration_authorization_rules_create_device_admin_policy_by_id_authorization_rule_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'commands': ['string'], 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': 'string', 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_38edb17577d9503ba1155c2916dcf663(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_38edb17577d9503ba1155c2916dcf663_PATTERN,
            self.path
        )

    def device_administration_authorization_rules_reset_hit_counts_device_admin_policy_by_id_authorization_rules_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'message': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_f1d11ab85a0a5597b9513d92a894ef1b(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_f1d11ab85a0a5597b9513d92a894ef1b_PATTERN,
            self.path
        )

    def device_administration_authorization_rules_get_device_admin_policy_by_id_authorization_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'commands': ['string'], 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': 'string', 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_80b60ed1eed75d7d9091344f4e38e2f1(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_80b60ed1eed75d7d9091344f4e38e2f1_PATTERN,
            self.path
        )

    def device_administration_authorization_rules_update_device_admin_policy_by_id_authorization_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'commands': ['string'], 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': 'string', 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_e7979abd11155f12b1336bbf02a99687(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_e7979abd11155f12b1336bbf02a99687_PATTERN,
            self.path
        )

    def device_administration_authorization_rules_delete_device_admin_policy_by_id_authorization_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_COMMAND_SET_273e0977618453b1b00e1c2b4cfa1999(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_COMMAND_SET_273e0977618453b1b00e1c2b4cfa1999_PATTERN,
            self.path
        )

    def device_administration_command_set_get_device_admin_command_sets_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps([{'id': 'string', 'name': 'string'}])
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_CONDITIONS_fdfa9b301f925a34a848f29f223e5b8d(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_CONDITIONS_fdfa9b301f925a34a848f29f223e5b8d_PATTERN,
            self.path
        )

    def device_administration_conditions_get_device_admin_conditions_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_CONDITIONS_b84dbd77c49f5056b9bf3c1e496ebe5f(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_CONDITIONS_b84dbd77c49f5056b9bf3c1e496ebe5f_PATTERN,
            self.path
        )

    def device_administration_conditions_post_device_admin_condition_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_CONDITIONS_316863dcb2ca563999b2d3691e1def79(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_CONDITIONS_316863dcb2ca563999b2d3691e1def79_PATTERN,
            self.path
        )

    def device_administration_conditions_get_device_admin_conditions_for_authentication_rule_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_CONDITIONS_e67076b912ef5362949be22842642596(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_CONDITIONS_e67076b912ef5362949be22842642596_PATTERN,
            self.path
        )

    def device_administration_conditions_get_device_admin_conditions_for_authorization_rule_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_CONDITIONS_3d9fe67eb28858609eca3907c8343015(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_CONDITIONS_3d9fe67eb28858609eca3907c8343015_PATTERN,
            self.path
        )

    def device_administration_conditions_get_device_admin_condition_by_condition_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_CONDITIONS_f0540adc16725e00adffdf57b67fb6ba(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_CONDITIONS_f0540adc16725e00adffdf57b67fb6ba_PATTERN,
            self.path
        )

    def device_administration_conditions_put_device_admin_condition_by_condition_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_CONDITIONS_c276cf1dc9545d45ae3f871966cb664b(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_CONDITIONS_c276cf1dc9545d45ae3f871966cb664b_PATTERN,
            self.path
        )

    def device_administration_conditions_delete_device_admin_condition_by_condition_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_CONDITIONS_68b404b307a35c2d9438da695bb49c54(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_CONDITIONS_68b404b307a35c2d9438da695bb49c54_PATTERN,
            self.path
        )

    def device_administration_conditions_get_device_admin_conditions_for_policy_set_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_CONDITIONS_27c0cf6ab73353ffa2b6986a9b16c54e(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_CONDITIONS_27c0cf6ab73353ffa2b6986a9b16c54e_PATTERN,
            self.path
        )

    def device_administration_conditions_get_device_admin_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_CONDITIONS_3b9b1bfd0f4151eb9812b474e4e4fa3c(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_CONDITIONS_3b9b1bfd0f4151eb9812b474e4e4fa3c_PATTERN,
            self.path
        )

    def device_administration_conditions_put_device_admin_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_CONDITIONS_2a6c1759c65b51a09ed7981397ece5c6(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_CONDITIONS_2a6c1759c65b51a09ed7981397ece5c6_PATTERN,
            self.path
        )

    def device_administration_conditions_delete_device_admin_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_DICTIONARY_ATTRIBUTES_LIST_7f1ff6e8bb2d5c7fbcf39fbadf5da2d5(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_DICTIONARY_ATTRIBUTES_LIST_7f1ff6e8bb2d5c7fbcf39fbadf5da2d5_PATTERN,
            self.path
        )

    def device_administration_dictionary_attributes_list_get_device_admin_dictionaries_authentication_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'allowedValues': [{'isDefault': True, 'key': 'string', 'value': 'string'}], 'dataType': 'string', 'description': 'string', 'dictionaryName': 'string', 'directionType': 'string', 'id': 'string', 'internalName': 'string', 'name': 'string'}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_DICTIONARY_ATTRIBUTES_LIST_6e2f955f29ce511993a189f2d234048d(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_DICTIONARY_ATTRIBUTES_LIST_6e2f955f29ce511993a189f2d234048d_PATTERN,
            self.path
        )

    def device_administration_dictionary_attributes_list_get_device_admin_dictionaries_authorization_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'allowedValues': [{'isDefault': True, 'key': 'string', 'value': 'string'}], 'dataType': 'string', 'description': 'string', 'dictionaryName': 'string', 'directionType': 'string', 'id': 'string', 'internalName': 'string', 'name': 'string'}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_DICTIONARY_ATTRIBUTES_LIST_892e064032895c8098927d3a39ef6af2(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_DICTIONARY_ATTRIBUTES_LIST_892e064032895c8098927d3a39ef6af2_PATTERN,
            self.path
        )

    def device_administration_dictionary_attributes_list_get_device_admin_dictionaries_policyset_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'allowedValues': [{'isDefault': True, 'key': 'string', 'value': 'string'}], 'dataType': 'string', 'description': 'string', 'dictionaryName': 'string', 'directionType': 'string', 'id': 'string', 'internalName': 'string', 'name': 'string'}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_IDENTITY_STORES_7ae7d98a7b185837af8d15ae864616e0(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_IDENTITY_STORES_7ae7d98a7b185837af8d15ae864616e0_PATTERN,
            self.path
        )

    def device_administration_identity_stores_get_device_admin_identity_stores_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps([{'id': 'string', 'name': 'string'}])
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_bda58fc63575503b80c024dbe02cf547(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_bda58fc63575503b80c024dbe02cf547_PATTERN,
            self.path
        )

    def device_administration_network_conditions_get_device_admin_network_conditions_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'conditionType': 'string', 'description': 'string', 'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'cliDnisList': ['string'], 'ipAddrList': ['string'], 'macAddrList': ['string'], 'deviceGroupList': ['string'], 'deviceList': ['string']}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_83ea4e38c44e5b1c90b19af25b88546e(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_83ea4e38c44e5b1c90b19af25b88546e_PATTERN,
            self.path
        )

    def device_administration_network_conditions_post_device_admin_network_condition_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'conditionType': 'string', 'description': 'string', 'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'cliDnisList': ['string'], 'ipAddrList': ['string'], 'macAddrList': ['string'], 'deviceGroupList': ['string'], 'deviceList': ['string']}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_a3640f918edb5df99d09001ca9e12688(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_a3640f918edb5df99d09001ca9e12688_PATTERN,
            self.path
        )

    def device_administration_network_conditions_get_device_admin_network_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'conditionType': 'string', 'description': 'string', 'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'cliDnisList': ['string'], 'ipAddrList': ['string'], 'macAddrList': ['string'], 'deviceGroupList': ['string'], 'deviceList': ['string']}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_b371441bddfd5d819a7aedfa215f4aeb(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_b371441bddfd5d819a7aedfa215f4aeb_PATTERN,
            self.path
        )

    def device_administration_network_conditions_put_device_admin_network_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'conditionType': 'string', 'description': 'string', 'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'cliDnisList': ['string'], 'ipAddrList': ['string'], 'macAddrList': ['string'], 'deviceGroupList': ['string'], 'deviceList': ['string']}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_037e7b011df45066b55be86033ecd17a(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_037e7b011df45066b55be86033ecd17a_PATTERN,
            self.path
        )

    def device_administration_network_conditions_delete_device_admin_network_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_POLICY_SET_923587ed5920513e92b1728b824771cc(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_POLICY_SET_923587ed5920513e92b1728b824771cc_PATTERN,
            self.path
        )

    def device_administration_policy_set_get_device_admin_policy_set_list_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}, 'default': True, 'description': 'string', 'hitCounts': 0, 'id': 'string', 'isProxy': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'rank': 0, 'serviceName': 'string', 'state': 'string'}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_POLICY_SET_5767ac3ccf225801ad8ba0bb1ad9de0b(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_POLICY_SET_5767ac3ccf225801ad8ba0bb1ad9de0b_PATTERN,
            self.path
        )

    def device_administration_policy_set_create_device_admin_policy_set_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'description': 'string', 'hitCounts': 0, 'id': 'string', 'isProxy': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'rank': 0, 'serviceName': 'string', 'state': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_POLICY_SET_ed47964d442d52dca1f7da967f37b3e2(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_POLICY_SET_ed47964d442d52dca1f7da967f37b3e2_PATTERN,
            self.path
        )

    def device_administration_policy_set_reset_hit_counts_device_admin_policy_sets_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'message': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_POLICY_SET_49f36918d98a546ab6ca2618d1844984(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_POLICY_SET_49f36918d98a546ab6ca2618d1844984_PATTERN,
            self.path
        )

    def device_administration_policy_set_get_device_admin_policy_set_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'description': 'string', 'hitCounts': 0, 'id': 'string', 'isProxy': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'rank': 0, 'serviceName': 'string', 'state': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_POLICY_SET_b6cc40e0f4b45e8da5908776d124ed5a(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_POLICY_SET_b6cc40e0f4b45e8da5908776d124ed5a_PATTERN,
            self.path
        )

    def device_administration_policy_set_update_device_admin_policy_set_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'description': 'string', 'hitCounts': 0, 'id': 'string', 'isProxy': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'rank': 0, 'serviceName': 'string', 'state': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_POLICY_SET_f602e2f88378502a8d8bca6dff274afe(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_POLICY_SET_f602e2f88378502a8d8bca6dff274afe_PATTERN,
            self.path
        )

    def device_administration_policy_set_delete_device_admin_policy_set_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_PROFILES_8ca669963ed0563e96bb009bf14a417b(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_PROFILES_8ca669963ed0563e96bb009bf14a417b_PATTERN,
            self.path
        )

    def device_administration_profiles_get_device_admin_profiles_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps([{'id': 'string', 'name': 'string'}])
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_SERVICE_NAMES_36e8018e15b053f39046b5bec0243d3f(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_SERVICE_NAMES_36e8018e15b053f39046b5bec0243d3f_PATTERN,
            self.path
        )

    def device_administration_service_names_get_device_admin_service_names_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps([{'id': 'string', 'isLocalAuthorization': True, 'name': 'string', 'serviceType': 'string'}])
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_816bf923264c53f98d5c347fa50b9c15(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_816bf923264c53f98d5c347fa50b9c15_PATTERN,
            self.path
        )

    def device_administration_time_date_conditions_get_device_admin_time_conditions_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_98b30f809e275589bd7154b5b4093d3f(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_98b30f809e275589bd7154b5b4093d3f_PATTERN,
            self.path
        )

    def device_administration_time_date_conditions_post_device_admin_time_condition_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_15ffd94d339a5fea8a4777dccccb926f(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_15ffd94d339a5fea8a4777dccccb926f_PATTERN,
            self.path
        )

    def device_administration_time_date_conditions_get_device_admin_time_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_e3241242740252b2814e0b474c314e9b(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_e3241242740252b2814e0b474c314e9b_PATTERN,
            self.path
        )

    def device_administration_time_date_conditions_put_device_admin_time_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_cf9f01129179555aa60c446f0a65c65a(self):
        return re.search(
            self.DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_cf9f01129179555aa60c446f0a65c65a_PATTERN,
            self.path
        )

    def device_administration_time_date_conditions_delete_device_admin_time_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHENTICATION_RULES_7956d836da955609bd9a5243101f3536(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHENTICATION_RULES_7956d836da955609bd9a5243101f3536_PATTERN,
            self.path
        )

    def network_access_authentication_rules_get_network_access_policy_by_id_authentication_rule_list_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'identitySourceName': 'string', 'ifAuthFail': 'string', 'ifProcessFail': 'string', 'ifUserNotFound': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHENTICATION_RULES_c26e318c3c405713a55b4e162be8c890(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHENTICATION_RULES_c26e318c3c405713a55b4e162be8c890_PATTERN,
            self.path
        )

    def network_access_authentication_rules_create_network_access_policy_by_id_authentication_rule_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'identitySourceName': 'string', 'ifAuthFail': 'string', 'ifProcessFail': 'string', 'ifUserNotFound': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHENTICATION_RULES_362ffc5178ed53749ebcaadd1c2af785(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHENTICATION_RULES_362ffc5178ed53749ebcaadd1c2af785_PATTERN,
            self.path
        )

    def network_access_authentication_rules_reset_hit_counts_network_access_policy_by_id_authentication_rules_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'message': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHENTICATION_RULES_85a98a9a386755939fe1f1633be33689(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHENTICATION_RULES_85a98a9a386755939fe1f1633be33689_PATTERN,
            self.path
        )

    def network_access_authentication_rules_get_network_access_policy_by_id_authentication_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'identitySourceName': 'string', 'ifAuthFail': 'string', 'ifProcessFail': 'string', 'ifUserNotFound': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHENTICATION_RULES_ec5180b8603d5cf78c13d6d3c0be18c2(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHENTICATION_RULES_ec5180b8603d5cf78c13d6d3c0be18c2_PATTERN,
            self.path
        )

    def network_access_authentication_rules_update_network_access_policy_by_id_authentication_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'identitySourceName': 'string', 'ifAuthFail': 'string', 'ifProcessFail': 'string', 'ifUserNotFound': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHENTICATION_RULES_da4f3b797ace547fa8f298d8c5197ce8(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHENTICATION_RULES_da4f3b797ace547fa8f298d8c5197ce8_PATTERN,
            self.path
        )

    def network_access_authentication_rules_delete_network_access_policy_by_id_authentication_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_9b2117ae65635dfd9c9d7042eb649261(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_9b2117ae65635dfd9c9d7042eb649261_PATTERN,
            self.path
        )

    def network_access_authorization_exception_rules_get_network_access_policy_by_id_local_exception_rule_list_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': ['string'], 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}, 'securityGroup': 'string'}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_2d40ae38628c51c49af42a4ede3d66d9(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_2d40ae38628c51c49af42a4ede3d66d9_PATTERN,
            self.path
        )

    def network_access_authorization_exception_rules_create_network_access_policy_by_id_local_exception_rule_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': ['string'], 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}, 'securityGroup': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_7d45668b438c59a6b92eb3c79386935b(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_7d45668b438c59a6b92eb3c79386935b_PATTERN,
            self.path
        )

    def network_access_authorization_exception_rules_reset_hit_counts_network_access_policy_by_id_local_exceptions_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'message': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_d01cc518eafd5daeaf80b7e83f4d6ad1(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_d01cc518eafd5daeaf80b7e83f4d6ad1_PATTERN,
            self.path
        )

    def network_access_authorization_exception_rules_get_network_access_policy_by_id_local_exception_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': ['string'], 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}, 'securityGroup': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_d5c906da96395858b888f382e2ab9d79(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_d5c906da96395858b888f382e2ab9d79_PATTERN,
            self.path
        )

    def network_access_authorization_exception_rules_update_network_access_policy_by_id_local_exception_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': ['string'], 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}, 'securityGroup': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_0d60e4de79065869a39a937f02e3e885(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_0d60e4de79065869a39a937f02e3e885_PATTERN,
            self.path
        )

    def network_access_authorization_exception_rules_delete_network_access_policy_by_id_local_exception_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_8de9a19a8393543da5814b1dce75abf6(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_8de9a19a8393543da5814b1dce75abf6_PATTERN,
            self.path
        )

    def network_access_authorization_global_exception_rules_get_network_access_policy_set_global_exception_rule_list_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': ['string'], 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}, 'securityGroup': 'string'}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_f9df6a3c6cf953319db3b8c36720997d(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_f9df6a3c6cf953319db3b8c36720997d_PATTERN,
            self.path
        )

    def network_access_authorization_global_exception_rules_create_network_access_policy_set_global_exception_rule_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': ['string'], 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}, 'securityGroup': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_31254fb8a2895e8982180d5f9339f8e4(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_31254fb8a2895e8982180d5f9339f8e4_PATTERN,
            self.path
        )

    def network_access_authorization_global_exception_rules_reset_hit_counts_network_access_global_exceptions_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'message': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_9b71b104d553520aafc4ce52b537a482(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_9b71b104d553520aafc4ce52b537a482_PATTERN,
            self.path
        )

    def network_access_authorization_global_exception_rules_get_network_access_policy_set_global_exception_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': ['string'], 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}, 'securityGroup': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_42639223458c51c99e8f35329c276126(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_42639223458c51c99e8f35329c276126_PATTERN,
            self.path
        )

    def network_access_authorization_global_exception_rules_update_network_access_policy_set_global_exception_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': ['string'], 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}, 'securityGroup': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_61e00af18a485a9283811feb84b04843(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_61e00af18a485a9283811feb84b04843_PATTERN,
            self.path
        )

    def network_access_authorization_global_exception_rules_delete_network_access_policy_set_global_exception_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_RULES_565fef1c1b1c53eeb784322caec31573(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_RULES_565fef1c1b1c53eeb784322caec31573_PATTERN,
            self.path
        )

    def network_access_authorization_rules_get_network_access_policy_by_id_authorization_rule_list_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': ['string'], 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}, 'securityGroup': 'string'}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_RULES_b9de636ff2e25f849f468556c53b7b9a(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_RULES_b9de636ff2e25f849f468556c53b7b9a_PATTERN,
            self.path
        )

    def network_access_authorization_rules_create_network_access_policy_by_id_authorization_rule_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': ['string'], 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}, 'securityGroup': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_RULES_e263dfc3d6e5513fa6ae916a22d14e5d(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_RULES_e263dfc3d6e5513fa6ae916a22d14e5d_PATTERN,
            self.path
        )

    def network_access_authorization_rules_reset_hit_counts_network_access_policy_by_id_authorization_rules_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'message': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_RULES_b19f79dd969d5444a6ba7b2acbf0f3cf(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_RULES_b19f79dd969d5444a6ba7b2acbf0f3cf_PATTERN,
            self.path
        )

    def network_access_authorization_rules_get_network_access_policy_by_id_authorization_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': ['string'], 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}, 'securityGroup': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_RULES_a8c6432bf3c8523e9876c4ac9d92c8b5(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_RULES_a8c6432bf3c8523e9876c4ac9d92c8b5_PATTERN,
            self.path
        )

    def network_access_authorization_rules_update_network_access_policy_by_id_authorization_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'profile': ['string'], 'rule': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}, 'securityGroup': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_AUTHORIZATION_RULES_0f8c47fa229d5f749f7432510709876c(self):
        return re.search(
            self.NETWORK_ACCESS_AUTHORIZATION_RULES_0f8c47fa229d5f749f7432510709876c_PATTERN,
            self.path
        )

    def network_access_authorization_rules_delete_network_access_policy_by_id_authorization_rule_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_CONDITIONS_daaac00241cc57a1a360043cbce63df6(self):
        return re.search(
            self.NETWORK_ACCESS_CONDITIONS_daaac00241cc57a1a360043cbce63df6_PATTERN,
            self.path
        )

    def network_access_conditions_get_network_access_conditions_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_CONDITIONS_36e5dd2909045a90bdce4848865662c2(self):
        return re.search(
            self.NETWORK_ACCESS_CONDITIONS_36e5dd2909045a90bdce4848865662c2_PATTERN,
            self.path
        )

    def network_access_conditions_post_network_access_condition_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_CONDITIONS_3a155387e56e5f9ba511dc4e4c9f46b4(self):
        return re.search(
            self.NETWORK_ACCESS_CONDITIONS_3a155387e56e5f9ba511dc4e4c9f46b4_PATTERN,
            self.path
        )

    def network_access_conditions_get_network_access_conditions_for_authentication_rule_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_CONDITIONS_3e196799ee895b3981634d93ec48f58c(self):
        return re.search(
            self.NETWORK_ACCESS_CONDITIONS_3e196799ee895b3981634d93ec48f58c_PATTERN,
            self.path
        )

    def network_access_conditions_get_network_access_conditions_for_authorization_rule_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_CONDITIONS_9c98c10af4da50d99fb62c7097f07736(self):
        return re.search(
            self.NETWORK_ACCESS_CONDITIONS_9c98c10af4da50d99fb62c7097f07736_PATTERN,
            self.path
        )

    def network_access_conditions_get_network_access_condition_by_condition_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_CONDITIONS_bbc720f738bf5b83a20de7e28e3c4c5f(self):
        return re.search(
            self.NETWORK_ACCESS_CONDITIONS_bbc720f738bf5b83a20de7e28e3c4c5f_PATTERN,
            self.path
        )

    def network_access_conditions_put_network_access_condition_by_condition_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_CONDITIONS_1ccbc1ec86665500b4520ba48304eab7(self):
        return re.search(
            self.NETWORK_ACCESS_CONDITIONS_1ccbc1ec86665500b4520ba48304eab7_PATTERN,
            self.path
        )

    def network_access_conditions_delete_network_access_condition_by_condition_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_CONDITIONS_902bf0cf46ba5b60b00176d2897fc7d3(self):
        return re.search(
            self.NETWORK_ACCESS_CONDITIONS_902bf0cf46ba5b60b00176d2897fc7d3_PATTERN,
            self.path
        )

    def network_access_conditions_get_network_access_conditions_for_policy_set_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_CONDITIONS_150027701d3053acae2eb596718a9ca3(self):
        return re.search(
            self.NETWORK_ACCESS_CONDITIONS_150027701d3053acae2eb596718a9ca3_PATTERN,
            self.path
        )

    def network_access_conditions_get_network_access_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_CONDITIONS_1f0d3cb73c4e59208d9ee04ffa787b3c(self):
        return re.search(
            self.NETWORK_ACCESS_CONDITIONS_1f0d3cb73c4e59208d9ee04ffa787b3c_PATTERN,
            self.path
        )

    def network_access_conditions_put_network_access_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_CONDITIONS_010c97b4161c5b95a6a83b6917ce26d6(self):
        return re.search(
            self.NETWORK_ACCESS_CONDITIONS_010c97b4161c5b95a6a83b6917ce26d6_PATTERN,
            self.path
        )

    def network_access_conditions_delete_network_access_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_DICTIONARY_1eb2cef3895d5bc68b7a28eca42ef630(self):
        return re.search(
            self.NETWORK_ACCESS_DICTIONARY_1eb2cef3895d5bc68b7a28eca42ef630_PATTERN,
            self.path
        )

    def network_access_dictionary_get_network_access_dictionaries_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'description': 'string', 'dictionaryAttrType': 'string', 'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'version': 'string'}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_DICTIONARY_7205be755dae5251bd2d8348eeebfdde(self):
        return re.search(
            self.NETWORK_ACCESS_DICTIONARY_7205be755dae5251bd2d8348eeebfdde_PATTERN,
            self.path
        )

    def network_access_dictionary_post_network_access_dictionaries_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'description': 'string', 'dictionaryAttrType': 'string', 'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'version': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_DICTIONARY_e60234354578568697b6740d08170678(self):
        return re.search(
            self.NETWORK_ACCESS_DICTIONARY_e60234354578568697b6740d08170678_PATTERN,
            self.path
        )

    def network_access_dictionary_get_network_access_dictionary_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'description': 'string', 'dictionaryAttrType': 'string', 'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'version': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_DICTIONARY_e4f1e31aca1558f782a2cdb43853aaf2(self):
        return re.search(
            self.NETWORK_ACCESS_DICTIONARY_e4f1e31aca1558f782a2cdb43853aaf2_PATTERN,
            self.path
        )

    def network_access_dictionary_put_network_access_dictionaries_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'description': 'string', 'dictionaryAttrType': 'string', 'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'version': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_DICTIONARY_2b80087f14af51d186a7bfa89f5a494b(self):
        return re.search(
            self.NETWORK_ACCESS_DICTIONARY_2b80087f14af51d186a7bfa89f5a494b_PATTERN,
            self.path
        )

    def network_access_dictionary_delete_network_access_dictionaries_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'description': 'string', 'dictionaryAttrType': 'string', 'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'version': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_b47094632edd5daea17c82b5fcd812f5(self):
        return re.search(
            self.NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_b47094632edd5daea17c82b5fcd812f5_PATTERN,
            self.path
        )

    def network_access_dictionary_attribute_get_network_access_dictionary_attributes_by_dictionary_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'allowedValues': [{'isDefault': True, 'key': 'string', 'value': 'string'}], 'dataType': 'string', 'description': 'string', 'dictionaryName': 'string', 'directionType': 'string', 'id': 'string', 'internalName': 'string', 'name': 'string'}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_9d3034483aaa5563bb287ef0cd502130(self):
        return re.search(
            self.NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_9d3034483aaa5563bb287ef0cd502130_PATTERN,
            self.path
        )

    def network_access_dictionary_attribute_post_network_access_dictionaries_by_dictionary_name_attribute_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'allowedValues': [{'isDefault': True, 'key': 'string', 'value': 'string'}], 'dataType': 'string', 'description': 'string', 'dictionaryName': 'string', 'directionType': 'string', 'id': 'string', 'internalName': 'string', 'name': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_cb8619385d265527a56dc7a27527f3a1(self):
        return re.search(
            self.NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_cb8619385d265527a56dc7a27527f3a1_PATTERN,
            self.path
        )

    def network_access_dictionary_attribute_get_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'allowedValues': [{'isDefault': True, 'key': 'string', 'value': 'string'}], 'dataType': 'string', 'description': 'string', 'dictionaryName': 'string', 'directionType': 'string', 'id': 'string', 'internalName': 'string', 'name': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_d2810d771d3e5ec580c39e0deb46b2b8(self):
        return re.search(
            self.NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_d2810d771d3e5ec580c39e0deb46b2b8_PATTERN,
            self.path
        )

    def network_access_dictionary_attribute_put_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'allowedValues': [{'isDefault': True, 'key': 'string', 'value': 'string'}], 'dataType': 'string', 'description': 'string', 'dictionaryName': 'string', 'directionType': 'string', 'id': 'string', 'internalName': 'string', 'name': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_e1725efd8ea253d1930913a85709977f(self):
        return re.search(
            self.NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_e1725efd8ea253d1930913a85709977f_PATTERN,
            self.path
        )

    def network_access_dictionary_attribute_delete_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'allowedValues': [{'isDefault': True, 'key': 'string', 'value': 'string'}], 'dataType': 'string', 'description': 'string', 'dictionaryName': 'string', 'directionType': 'string', 'id': 'string', 'internalName': 'string', 'name': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_DICTIONARY_ATTRIBUTES_LIST_469345c8455c5c6fac438317f314f407(self):
        return re.search(
            self.NETWORK_ACCESS_DICTIONARY_ATTRIBUTES_LIST_469345c8455c5c6fac438317f314f407_PATTERN,
            self.path
        )

    def network_access_dictionary_attributes_list_get_network_access_dictionaries_authentication_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'allowedValues': [{'isDefault': True, 'key': 'string', 'value': 'string'}], 'dataType': 'string', 'description': 'string', 'dictionaryName': 'string', 'directionType': 'string', 'id': 'string', 'internalName': 'string', 'name': 'string'}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_DICTIONARY_ATTRIBUTES_LIST_e86076c61aa9548dacaf5eb77e98a20c(self):
        return re.search(
            self.NETWORK_ACCESS_DICTIONARY_ATTRIBUTES_LIST_e86076c61aa9548dacaf5eb77e98a20c_PATTERN,
            self.path
        )

    def network_access_dictionary_attributes_list_get_network_access_dictionaries_authorization_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'allowedValues': [{'isDefault': True, 'key': 'string', 'value': 'string'}], 'dataType': 'string', 'description': 'string', 'dictionaryName': 'string', 'directionType': 'string', 'id': 'string', 'internalName': 'string', 'name': 'string'}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_DICTIONARY_ATTRIBUTES_LIST_5bce945bea7456fd930ee327ece18828(self):
        return re.search(
            self.NETWORK_ACCESS_DICTIONARY_ATTRIBUTES_LIST_5bce945bea7456fd930ee327ece18828_PATTERN,
            self.path
        )

    def network_access_dictionary_attributes_list_get_network_access_dictionaries_policyset_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'allowedValues': [{'isDefault': True, 'key': 'string', 'value': 'string'}], 'dataType': 'string', 'description': 'string', 'dictionaryName': 'string', 'directionType': 'string', 'id': 'string', 'internalName': 'string', 'name': 'string'}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_IDENTITY_STORES_4ef75d8c1654508aae4fc2ee9b34fabc(self):
        return re.search(
            self.NETWORK_ACCESS_IDENTITY_STORES_4ef75d8c1654508aae4fc2ee9b34fabc_PATTERN,
            self.path
        )

    def network_access_identity_stores_get_network_access_identity_stores_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps([{'id': 'string', 'name': 'string'}])
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_NETWORK_CONDITIONS_da2d8b2763ed53d9bec7f9427c4ce344(self):
        return re.search(
            self.NETWORK_ACCESS_NETWORK_CONDITIONS_da2d8b2763ed53d9bec7f9427c4ce344_PATTERN,
            self.path
        )

    def network_access_network_conditions_get_network_access_network_conditions_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'conditionType': 'string', 'description': 'string', 'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'cliDnisList': ['string'], 'ipAddrList': ['string'], 'macAddrList': ['string'], 'deviceGroupList': ['string'], 'deviceList': ['string']}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_NETWORK_CONDITIONS_858ad86a47e15d45ab1cc0cadc5b248f(self):
        return re.search(
            self.NETWORK_ACCESS_NETWORK_CONDITIONS_858ad86a47e15d45ab1cc0cadc5b248f_PATTERN,
            self.path
        )

    def network_access_network_conditions_post_network_access_network_condition_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'conditionType': 'string', 'description': 'string', 'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'cliDnisList': ['string'], 'ipAddrList': ['string'], 'macAddrList': ['string'], 'deviceGroupList': ['string'], 'deviceList': ['string']}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_NETWORK_CONDITIONS_64faeb3bb3f25787844f6973d5a1658f(self):
        return re.search(
            self.NETWORK_ACCESS_NETWORK_CONDITIONS_64faeb3bb3f25787844f6973d5a1658f_PATTERN,
            self.path
        )

    def network_access_network_conditions_get_network_access_network_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'conditionType': 'string', 'description': 'string', 'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'cliDnisList': ['string'], 'ipAddrList': ['string'], 'macAddrList': ['string'], 'deviceGroupList': ['string'], 'deviceList': ['string']}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_NETWORK_CONDITIONS_5aaa481aaad35f8b8a7cbf2e063eac2b(self):
        return re.search(
            self.NETWORK_ACCESS_NETWORK_CONDITIONS_5aaa481aaad35f8b8a7cbf2e063eac2b_PATTERN,
            self.path
        )

    def network_access_network_conditions_put_network_access_network_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'conditionType': 'string', 'description': 'string', 'id': 'string', 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'cliDnisList': ['string'], 'ipAddrList': ['string'], 'macAddrList': ['string'], 'deviceGroupList': ['string'], 'deviceList': ['string']}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_NETWORK_CONDITIONS_8e345ca7adb75b1bacfa42771a4d242c(self):
        return re.search(
            self.NETWORK_ACCESS_NETWORK_CONDITIONS_8e345ca7adb75b1bacfa42771a4d242c_PATTERN,
            self.path
        )

    def network_access_network_conditions_delete_network_access_network_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_POLICY_SET_229b904117c35daf8833398c262c403d(self):
        return re.search(
            self.NETWORK_ACCESS_POLICY_SET_229b904117c35daf8833398c262c403d_PATTERN,
            self.path
        )

    def network_access_policy_set_get_network_access_policy_set_list_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}, 'default': True, 'description': 'string', 'hitCounts': 0, 'id': 'string', 'isProxy': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'rank': 0, 'serviceName': 'string', 'state': 'string'}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_POLICY_SET_42e1af4e392c5790a01685b9687208c0(self):
        return re.search(
            self.NETWORK_ACCESS_POLICY_SET_42e1af4e392c5790a01685b9687208c0_PATTERN,
            self.path
        )

    def network_access_policy_set_create_network_access_policy_set_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'description': 'string', 'hitCounts': 0, 'id': 'string', 'isProxy': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'rank': 0, 'serviceName': 'string', 'state': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_POLICY_SET_678aef73e11e56edb468869d663b5e85(self):
        return re.search(
            self.NETWORK_ACCESS_POLICY_SET_678aef73e11e56edb468869d663b5e85_PATTERN,
            self.path
        )

    def network_access_policy_set_reset_hit_counts_network_access_policy_sets_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'message': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_POLICY_SET_1fb3b6363bad54678ae56dc699e8c7e8(self):
        return re.search(
            self.NETWORK_ACCESS_POLICY_SET_1fb3b6363bad54678ae56dc699e8c7e8_PATTERN,
            self.path
        )

    def network_access_policy_set_get_network_access_policy_set_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'description': 'string', 'hitCounts': 0, 'id': 'string', 'isProxy': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'rank': 0, 'serviceName': 'string', 'state': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_POLICY_SET_4068064fa27e5a779143ed557b417535(self):
        return re.search(
            self.NETWORK_ACCESS_POLICY_SET_4068064fa27e5a779143ed557b417535_PATTERN,
            self.path
        )

    def network_access_policy_set_update_network_access_policy_set_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'description': 'string', 'hitCounts': 0, 'id': 'string', 'isProxy': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'name': 'string', 'rank': 0, 'serviceName': 'string', 'state': 'string'}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_POLICY_SET_c1d0c2c01a5856fa8be5af8e2b07e420(self):
        return re.search(
            self.NETWORK_ACCESS_POLICY_SET_c1d0c2c01a5856fa8be5af8e2b07e420_PATTERN,
            self.path
        )

    def network_access_policy_set_delete_network_access_policy_set_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_PROFILES_97b33c6c1bdf5c6b8c63835ce0298418(self):
        return re.search(
            self.NETWORK_ACCESS_PROFILES_97b33c6c1bdf5c6b8c63835ce0298418_PATTERN,
            self.path
        )

    def network_access_profiles_get_network_access_profiles_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps([{'id': 'string', 'name': 'string'}])
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_SECURITY_GROUPS_b92977dab6965e1c9fd86b96e4aa7e92(self):
        return re.search(
            self.NETWORK_ACCESS_SECURITY_GROUPS_b92977dab6965e1c9fd86b96e4aa7e92_PATTERN,
            self.path
        )

    def network_access_security_groups_get_network_access_security_groups_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps([{'id': 'string', 'name': 'string'}])
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_SERVICE_NAMES_ca8f50a31b325fd281ae7f7b69f31d3f(self):
        return re.search(
            self.NETWORK_ACCESS_SERVICE_NAMES_ca8f50a31b325fd281ae7f7b69f31d3f_PATTERN,
            self.path
        )

    def network_access_service_names_get_network_access_service_names_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps([{'id': 'string', 'isLocalAuthorization': True, 'name': 'string', 'serviceType': 'string'}])
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_TIME_DATE_CONDITIONS_1533f65d301c5ee3a66ac5220cac3348(self):
        return re.search(
            self.NETWORK_ACCESS_TIME_DATE_CONDITIONS_1533f65d301c5ee3a66ac5220cac3348_PATTERN,
            self.path
        )

    def network_access_time_date_conditions_get_network_access_time_conditions_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': [{}], 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_TIME_DATE_CONDITIONS_fc5800b01699562cb563664affdd7757(self):
        return re.search(
            self.NETWORK_ACCESS_TIME_DATE_CONDITIONS_fc5800b01699562cb563664affdd7757_PATTERN,
            self.path
        )

    def network_access_time_date_conditions_post_network_access_time_condition_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_TIME_DATE_CONDITIONS_e8c39503b29051bea788021a168833da(self):
        return re.search(
            self.NETWORK_ACCESS_TIME_DATE_CONDITIONS_e8c39503b29051bea788021a168833da_PATTERN,
            self.path
        )

    def network_access_time_date_conditions_get_network_access_time_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_TIME_DATE_CONDITIONS_fef057ddea8d56a98189b1db3bf5f240(self):
        return re.search(
            self.NETWORK_ACCESS_TIME_DATE_CONDITIONS_fef057ddea8d56a98189b1db3bf5f240_PATTERN,
            self.path
        )

    def network_access_time_date_conditions_put_network_access_time_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'response': {}, 'version': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_ACCESS_TIME_DATE_CONDITIONS_10517292296559f2847ac681d93cf40b(self):
        return re.search(
            self.NETWORK_ACCESS_TIME_DATE_CONDITIONS_10517292296559f2847ac681d93cf40b_PATTERN,
            self.path
        )

    def network_access_time_date_conditions_delete_network_access_time_condition_by_condition_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'id': 'string'})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACI_BINDINGS_3d1448851f0154d0b6e9c856ec6cc6f0(self):
        return re.search(
            self.ACI_BINDINGS_3d1448851f0154d0b6e9c856ec6cc6f0_PATTERN,
            self.path
        )

    def aci_bindings_get_all_aci_bindings_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ACIBindings': {'id': 'string', 'name': 'string', 'description': 'string', 'ip': 'string', 'sgtValue': 'string', 'vn': 'string', 'psn': 'string', 'learnedFrom': 'string', 'learnedBy': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACI_BINDINGS_d74b5214bad656c98f21e4968661c3c0(self):
        return re.search(
            self.ACI_BINDINGS_d74b5214bad656c98f21e4968661c3c0_PATTERN,
            self.path
        )

    def aci_bindings_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACI_SETTINGS_2ea5c865993b56f48f7f43475294a20c(self):
        return re.search(
            self.ACI_SETTINGS_2ea5c865993b56f48f7f43475294a20c_PATTERN,
            self.path
        )

    def aci_settings_get_all_aci_settings_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'AciSettings': {'id': 'string', 'enableAci': True, 'ipAddressHostName': 'string', 'adminName': 'string', 'tenantName': 'string', 'l3RouteNetwork': 'string', 'suffixToEpg': 'string', 'suffixToSgt': 'string', 'allSxpDomain': True, 'specificSxpDomain': True, 'specifixSxpDomainList': ['string'], 'enableDataPlane': True, 'untaggedPacketIepgName': 'string', 'defaultSgtName': 'string', 'enableElementsLimit': True, 'maxNumIepgFromAci': 0, 'maxNumSgtToAci': 0, 'aci50': True, 'aci51': True}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACI_SETTINGS_1b155c91eec153338302d492db1afb80(self):
        return re.search(
            self.ACI_SETTINGS_1b155c91eec153338302d492db1afb80_PATTERN,
            self.path
        )

    def aci_settings_test_aci_connectivity_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ACITestConnectionResult': {'result': True}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACI_SETTINGS_56cea2e785ee57908a9ee3b118e49cfa(self):
        return re.search(
            self.ACI_SETTINGS_56cea2e785ee57908a9ee3b118e49cfa_PATTERN,
            self.path
        )

    def aci_settings_update_aci_settings_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACI_SETTINGS_462410ea47f65521bcf0ab949b5d72b5(self):
        return re.search(
            self.ACI_SETTINGS_462410ea47f65521bcf0ab949b5d72b5_PATTERN,
            self.path
        )

    def aci_settings_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACTIVE_DIRECTORY_7c6be021c4ca59e48c97afe218219bb1(self):
        return re.search(
            self.ACTIVE_DIRECTORY_7c6be021c4ca59e48c97afe218219bb1_PATTERN,
            self.path
        )

    def active_directory_get_active_directory_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSActiveDirectory': {'id': 'string', 'name': 'string', 'description': 'string', 'domain': 'string', 'enableDomainAllowedList': True, 'enableDomainWhiteList': True, 'adgroups': {'groups': [{'name': 'string', 'sid': 'string', 'type': 'string'}]}, 'advancedSettings': {'enablePassChange': True, 'enableMachineAuth': True, 'enableMachineAccess': True, 'agingTime': 0, 'enableDialinPermissionCheck': True, 'enableCallbackForDialinClient': True, 'plaintextAuth': True, 'enableFailedAuthProtection': True, 'authProtectionType': 'string', 'failedAuthThreshold': 0, 'identityNotInAdBehaviour': 'string', 'unreachableDomainsBehaviour': 'string', 'enableRewrites': True, 'rewriteRules': [{'rowId': 0, 'rewriteMatch': 'string', 'rewriteResult': 'string'}], 'firstName': 'string', 'department': 'string', 'lastName': 'string', 'organizationalUnit': 'string', 'jobTitle': 'string', 'locality': 'string', 'email': 'string', 'stateOrProvince': 'string', 'telephone': 'string', 'country': 'string', 'streetAddress': 'string', 'schema': 'string'}, 'adAttributes': {'attributes': [{'name': 'string', 'type': 'string', 'internalName': 'string', 'defaultValue': 'string'}]}, 'adScopesNames': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACTIVE_DIRECTORY_b839d4dee9b958e48ccef056603e253f(self):
        return re.search(
            self.ACTIVE_DIRECTORY_b839d4dee9b958e48ccef056603e253f_PATTERN,
            self.path
        )

    def active_directory_get_all_user_groups_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSActiveDirectory': {'groups': [{'groupName': 'string', 'sid': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACTIVE_DIRECTORY_14104b05e80058df96e685baa727d578(self):
        return re.search(
            self.ACTIVE_DIRECTORY_14104b05e80058df96e685baa727d578_PATTERN,
            self.path
        )

    def active_directory_load_groups_from_domain_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACTIVE_DIRECTORY_8091e84541805d1da1fa3d4d581102a9(self):
        return re.search(
            self.ACTIVE_DIRECTORY_8091e84541805d1da1fa3d4d581102a9_PATTERN,
            self.path
        )

    def active_directory_leave_domain_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACTIVE_DIRECTORY_eae60ece5110590e97ddd910e8144ed2(self):
        return re.search(
            self.ACTIVE_DIRECTORY_eae60ece5110590e97ddd910e8144ed2_PATTERN,
            self.path
        )

    def active_directory_is_user_member_of_groups_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSActiveDirectory': {'groups': [{'groupName': 'string', 'sid': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACTIVE_DIRECTORY_7d0ed84901325292ad4e2a91a174f6b2(self):
        return re.search(
            self.ACTIVE_DIRECTORY_7d0ed84901325292ad4e2a91a174f6b2_PATTERN,
            self.path
        )

    def active_directory_get_all_trusted_domains_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSActiveDirectoryDomains': {'domains': [{'dnsName': 'string', 'forest': 'string', 'unusableReason': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACTIVE_DIRECTORY_e84705b918955b53afe61fc37911eb8b(self):
        return re.search(
            self.ACTIVE_DIRECTORY_e84705b918955b53afe61fc37911eb8b_PATTERN,
            self.path
        )

    def active_directory_join_domain_with_all_nodes_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACTIVE_DIRECTORY_d011417d18d055ccb864c1dc2ae0456d(self):
        return re.search(
            self.ACTIVE_DIRECTORY_d011417d18d055ccb864c1dc2ae0456d_PATTERN,
            self.path
        )

    def active_directory_leave_domain_with_all_nodes_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACTIVE_DIRECTORY_48fd729f50e65695966359b589a1606b(self):
        return re.search(
            self.ACTIVE_DIRECTORY_48fd729f50e65695966359b589a1606b_PATTERN,
            self.path
        )

    def active_directory_get_groups_by_domain_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'groups': [{'groupName': 'string', 'sid': 'string', 'type': 'string'}]})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACTIVE_DIRECTORY_15236cfcc7615d0492e2dd1b04dd03a9(self):
        return re.search(
            self.ACTIVE_DIRECTORY_15236cfcc7615d0492e2dd1b04dd03a9_PATTERN,
            self.path
        )

    def active_directory_get_active_directory_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSActiveDirectory': {'id': 'string', 'name': 'string', 'description': 'string', 'domain': 'string', 'enableDomainWhiteList': True, 'enableDomainAllowedList': True, 'adgroups': {'groups': [{'name': 'string', 'sid': 'string', 'type': 'string'}]}, 'advancedSettings': {'enablePassChange': True, 'enableMachineAuth': True, 'enableMachineAccess': True, 'agingTime': 0, 'enableDialinPermissionCheck': True, 'enableCallbackForDialinClient': True, 'plaintextAuth': True, 'enableFailedAuthProtection': True, 'authProtectionType': 'string', 'failedAuthThreshold': 0, 'identityNotInAdBehaviour': 'string', 'unreachableDomainsBehaviour': 'string', 'enableRewrites': True, 'rewriteRules': [{'rowId': 0, 'rewriteMatch': 'string', 'rewriteResult': 'string'}], 'firstName': 'string', 'department': 'string', 'lastName': 'string', 'organizationalUnit': 'string', 'jobTitle': 'string', 'locality': 'string', 'email': 'string', 'stateOrProvince': 'string', 'telephone': 'string', 'country': 'string', 'streetAddress': 'string', 'schema': 'string'}, 'adAttributes': {'attributes': [{'name': 'string', 'type': 'string', 'internalName': 'string', 'defaultValue': 'string'}]}, 'adScopesNames': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACTIVE_DIRECTORY_786febbe79ed5bb780d97a98f292b606(self):
        return re.search(
            self.ACTIVE_DIRECTORY_786febbe79ed5bb780d97a98f292b606_PATTERN,
            self.path
        )

    def active_directory_delete_active_directory_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACTIVE_DIRECTORY_b3284240745e5b929c51495fe80bc1c4(self):
        return re.search(
            self.ACTIVE_DIRECTORY_b3284240745e5b929c51495fe80bc1c4_PATTERN,
            self.path
        )

    def active_directory_join_domain_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACTIVE_DIRECTORY_c8dbec9679d453f78cb47d894c507a7b(self):
        return re.search(
            self.ACTIVE_DIRECTORY_c8dbec9679d453f78cb47d894c507a7b_PATTERN,
            self.path
        )

    def active_directory_get_all_active_directory_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACTIVE_DIRECTORY_64e9318040a456978757d7abfa3e66b1(self):
        return re.search(
            self.ACTIVE_DIRECTORY_64e9318040a456978757d7abfa3e66b1_PATTERN,
            self.path
        )

    def active_directory_create_active_directory_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ACTIVE_DIRECTORY_c2d0923990e35be1882e4dee000254a9(self):
        return re.search(
            self.ACTIVE_DIRECTORY_c2d0923990e35be1882e4dee000254a9_PATTERN,
            self.path
        )

    def active_directory_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ADMIN_USER_adac9b81d9235be3b656acf9436583dd(self):
        return re.search(
            self.ADMIN_USER_adac9b81d9235be3b656acf9436583dd_PATTERN,
            self.path
        )

    def admin_user_get_admin_user_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'AdminUser': {'name': 'string', 'id': 'string', 'description': 'string', 'enabled': True, 'password': 'string', 'changePassword': True, 'includeSystemAlarmsInEmail': True, 'externalUser': True, 'inactiveAccountNeverDisabled': True, 'adminGroups': 'string', 'customAttributes': {}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ADMIN_USER_463a109d72fa5ac0a64d357302f26669(self):
        return re.search(
            self.ADMIN_USER_463a109d72fa5ac0a64d357302f26669_PATTERN,
            self.path
        )

    def admin_user_get_all_admin_users_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ADMIN_USER_9535a5edeb5057839d702e0f490dc28f(self):
        return re.search(
            self.ADMIN_USER_9535a5edeb5057839d702e0f490dc28f_PATTERN,
            self.path
        )

    def admin_user_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ALLOWED_PROTOCOLS_010ac8c8cb9b5007a1e1a6434a20a881(self):
        return re.search(
            self.ALLOWED_PROTOCOLS_010ac8c8cb9b5007a1e1a6434a20a881_PATTERN,
            self.path
        )

    def allowed_protocols_get_allowed_protocol_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'AllowedProtocols': {'id': 'string', 'name': 'string', 'description': 'string', 'eapTls': {'allowEapTlsAuthOfExpiredCerts': True, 'eapTlsEnableStatelessSessionResume': True, 'eapTlsSessionTicketTtl': 0, 'eapTlsSessionTicketTtlUnits': 'string', 'eapTlsSessionTicketPrecentage': 0}, 'peap': {'allowPeapEapMsChapV2': True, 'allowPeapEapMsChapV2PwdChange': True, 'allowPeapEapMsChapV2PwdChangeRetries': 0, 'allowPeapEapGtc': True, 'allowPeapEapGtcPwdChange': True, 'allowPeapEapGtcPwdChangeRetries': 0, 'allowPeapEapTls': True, 'allowPeapEapTlsAuthOfExpiredCerts': True, 'requireCryptobinding': True, 'allowPeapV0': True}, 'eapFast': {'allowEapFastEapMsChapV2': True, 'allowEapFastEapMsChapV2PwdChange': True, 'allowEapFastEapMsChapV2PwdChangeRetries': 0, 'allowEapFastEapGtc': True, 'allowEapFastEapGtcPwdChange': True, 'allowEapFastEapGtcPwdChangeRetries': 0, 'allowEapFastEapTls': True, 'allowEapFastEapTlsAuthOfExpiredCerts': True, 'eapFastUsePacs': True, 'eapFastUsePacsTunnelPacTtl': 0, 'eapFastUsePacsTunnelPacTtlUnits': 'string', 'eapFastUsePacsUseProactivePacUpdatePrecentage': 0, 'eapFastUsePacsAllowAnonymProvisioning': True, 'eapFastUsePacsAllowAuthenProvisioning': True, 'eapFastUsePacsReturnAccessAcceptAfterAuthenticatedProvisioning': True, 'eapFastUsePacsAcceptClientCert': True, 'eapFastUsePacsMachinePacTtl': 0, 'eapFastUsePacsMachinePacTtlUnits': 'string', 'eapFastUsePacsAllowMachineAuthentication': True, 'eapFastUsePacsStatelessSessionResume': True, 'eapFastUsePacsAuthorizationPacTtl': 0, 'eapFastUsePacsAuthorizationPacTtlUnits': 'string', 'eapFastDontUsePacsAcceptClientCert': True, 'eapFastDontUsePacsAllowMachineAuthentication': True, 'eapFastEnableEAPChaining': True}, 'eapTtls': {'eapTtlsPapAscii': True, 'eapTtlsChap': True, 'eapTtlsMsChapV1': True, 'eapTtlsMsChapV2': True, 'eapTtlsEapMd5': True, 'eapTtlsEapMsChapV2': True, 'eapTtlsEapMsChapV2PwdChange': True, 'eapTtlsEapMsChapV2PwdChangeRetries': 0}, 'teap': {'allowTeapEapMsChapV2': True, 'allowTeapEapMsChapV2PwdChange': True, 'allowTeapEapMsChapV2PwdChangeRetries': 0, 'allowTeapEapTls': True, 'allowTeapEapTlsAuthOfExpiredCerts': True, 'acceptClientCertDuringTunnelEst': True, 'enableEapChaining': True, 'allowDowngradeMsk': True}, 'processHostLookup': True, 'allowPapAscii': True, 'allowChap': True, 'allowMsChapV1': True, 'allowMsChapV2': True, 'allowEapMd5': True, 'allowLeap': True, 'allowEapTls': True, 'allowEapTtls': True, 'allowEapFast': True, 'allowPeap': True, 'allowTeap': True, 'allowPreferredEapProtocol': True, 'preferredEapProtocol': 'string', 'eapTlsLBit': True, 'allowWeakCiphersForEap': True, 'requireMessageAuth': True, 'link1': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ALLOWED_PROTOCOLS_696e3ddfddd45e299f14ed194926f8de(self):
        return re.search(
            self.ALLOWED_PROTOCOLS_696e3ddfddd45e299f14ed194926f8de_PATTERN,
            self.path
        )

    def allowed_protocols_get_allowed_protocol_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'AllowedProtocols': {'id': 'string', 'name': 'string', 'description': 'string', 'eapTls': {'allowEapTlsAuthOfExpiredCerts': True, 'eapTlsEnableStatelessSessionResume': True, 'eapTlsSessionTicketTtl': 0, 'eapTlsSessionTicketTtlUnits': 'string', 'eapTlsSessionTicketPrecentage': 0}, 'peap': {'allowPeapEapMsChapV2': True, 'allowPeapEapMsChapV2PwdChange': True, 'allowPeapEapMsChapV2PwdChangeRetries': 0, 'allowPeapEapGtc': True, 'allowPeapEapGtcPwdChange': True, 'allowPeapEapGtcPwdChangeRetries': 0, 'allowPeapEapTls': True, 'allowPeapEapTlsAuthOfExpiredCerts': True, 'requireCryptobinding': True, 'allowPeapV0': True}, 'eapFast': {'allowEapFastEapMsChapV2': True, 'allowEapFastEapMsChapV2PwdChange': True, 'allowEapFastEapMsChapV2PwdChangeRetries': 0, 'allowEapFastEapGtc': True, 'allowEapFastEapGtcPwdChange': True, 'allowEapFastEapGtcPwdChangeRetries': 0, 'allowEapFastEapTls': True, 'allowEapFastEapTlsAuthOfExpiredCerts': True, 'eapFastUsePacs': True, 'eapFastUsePacsTunnelPacTtl': 0, 'eapFastUsePacsTunnelPacTtlUnits': 'string', 'eapFastUsePacsUseProactivePacUpdatePrecentage': 0, 'eapFastUsePacsAllowAnonymProvisioning': True, 'eapFastUsePacsAllowAuthenProvisioning': True, 'eapFastUsePacsReturnAccessAcceptAfterAuthenticatedProvisioning': True, 'eapFastUsePacsAcceptClientCert': True, 'eapFastUsePacsMachinePacTtl': 0, 'eapFastUsePacsMachinePacTtlUnits': 'string', 'eapFastUsePacsAllowMachineAuthentication': True, 'eapFastUsePacsStatelessSessionResume': True, 'eapFastUsePacsAuthorizationPacTtl': 0, 'eapFastUsePacsAuthorizationPacTtlUnits': 'string', 'eapFastDontUsePacsAcceptClientCert': True, 'eapFastDontUsePacsAllowMachineAuthentication': True, 'eapFastEnableEAPChaining': True}, 'eapTtls': {'eapTtlsPapAscii': True, 'eapTtlsChap': True, 'eapTtlsMsChapV1': True, 'eapTtlsMsChapV2': True, 'eapTtlsEapMd5': True, 'eapTtlsEapMsChapV2': True, 'eapTtlsEapMsChapV2PwdChange': True, 'eapTtlsEapMsChapV2PwdChangeRetries': 0}, 'teap': {'allowTeapEapMsChapV2': True, 'allowTeapEapMsChapV2PwdChange': True, 'allowTeapEapMsChapV2PwdChangeRetries': 0, 'allowTeapEapTls': True, 'allowTeapEapTlsAuthOfExpiredCerts': True, 'acceptClientCertDuringTunnelEst': True, 'enableEapChaining': True, 'allowDowngradeMsk': True}, 'processHostLookup': True, 'allowPapAscii': True, 'allowChap': True, 'allowMsChapV1': True, 'allowMsChapV2': True, 'allowEapMd5': True, 'allowLeap': True, 'allowEapTls': True, 'allowEapTtls': True, 'allowEapFast': True, 'allowPeap': True, 'allowTeap': True, 'allowPreferredEapProtocol': True, 'preferredEapProtocol': 'string', 'eapTlsLBit': True, 'allowWeakCiphersForEap': True, 'requireMessageAuth': True, 'link1': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ALLOWED_PROTOCOLS_61a0b312f70257b1bfa90d0260f0c971(self):
        return re.search(
            self.ALLOWED_PROTOCOLS_61a0b312f70257b1bfa90d0260f0c971_PATTERN,
            self.path
        )

    def allowed_protocols_update_allowed_protocol_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ALLOWED_PROTOCOLS_a6cbd2c420785cfcbdecc3495bca8af4(self):
        return re.search(
            self.ALLOWED_PROTOCOLS_a6cbd2c420785cfcbdecc3495bca8af4_PATTERN,
            self.path
        )

    def allowed_protocols_delete_allowed_protocol_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ALLOWED_PROTOCOLS_d82fe0f9e4635b74af809beaaf98bd07(self):
        return re.search(
            self.ALLOWED_PROTOCOLS_d82fe0f9e4635b74af809beaaf98bd07_PATTERN,
            self.path
        )

    def allowed_protocols_get_all_allowed_protocols_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ALLOWED_PROTOCOLS_1b40ad23ab0a5a7b8adade320c8912e7(self):
        return re.search(
            self.ALLOWED_PROTOCOLS_1b40ad23ab0a5a7b8adade320c8912e7_PATTERN,
            self.path
        )

    def allowed_protocols_create_allowed_protocol_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ALLOWED_PROTOCOLS_c0f61393474f5744ab0a263a232d3b96(self):
        return re.search(
            self.ALLOWED_PROTOCOLS_c0f61393474f5744ab0a263a232d3b96_PATTERN,
            self.path
        )

    def allowed_protocols_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_AUTHORIZATION_PROFILE_acf0372068885036baee3c4524638f31(self):
        return re.search(
            self.AUTHORIZATION_PROFILE_acf0372068885036baee3c4524638f31_PATTERN,
            self.path
        )

    def authorization_profile_get_authorization_profile_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'AuthorizationProfile': {'id': 'string', 'name': 'string', 'description': 'string', 'advancedAttributes': [{'leftHandSideDictionaryAttribue': {'AdvancedAttributeValueType': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'value': 'string'}, 'rightHandSideAttribueValue': {'AdvancedAttributeValueType': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'value': 'string'}}], 'accessType': 'string', 'authzProfileType': 'string', 'vlan': {'nameID': 'string', 'tagID': 0}, 'reauth': {'timer': 0, 'connectivity': 'string'}, 'airespaceACL': 'string', 'airespaceIPv6ACL': 'string', 'webRedirection': {'WebRedirectionType': 'string', 'acl': 'string', 'portalName': 'string', 'staticIPHostNameFQDN': 'string', 'displayCertificatesRenewalMessages': True}, 'acl': 'string', 'trackMovement': True, 'agentlessPosture': True, 'serviceTemplate': True, 'easywiredSessionCandidate': True, 'daclName': 'string', 'voiceDomainPermission': True, 'neat': True, 'webAuth': True, 'autoSmartPort': 'string', 'interfaceTemplate': 'string', 'ipv6ACLFilter': 'string', 'avcProfile': 'string', 'macSecPolicy': 'string', 'asaVpn': 'string', 'profileName': 'string', 'ipv6DaclName': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_AUTHORIZATION_PROFILE_a69c7f1ad54e5e9cae1f871e19eed61b(self):
        return re.search(
            self.AUTHORIZATION_PROFILE_a69c7f1ad54e5e9cae1f871e19eed61b_PATTERN,
            self.path
        )

    def authorization_profile_get_authorization_profile_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'AuthorizationProfile': {'id': 'string', 'name': 'string', 'description': 'string', 'advancedAttributes': [{'leftHandSideDictionaryAttribue': {'AdvancedAttributeValueType': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'value': 'string'}, 'rightHandSideAttribueValue': {'AdvancedAttributeValueType': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'value': 'string'}}], 'accessType': 'string', 'authzProfileType': 'string', 'vlan': {'nameID': 'string', 'tagID': 0}, 'reauth': {'timer': 0, 'connectivity': 'string'}, 'airespaceACL': 'string', 'airespaceIPv6ACL': 'string', 'webRedirection': {'WebRedirectionType': 'string', 'acl': 'string', 'portalName': 'string', 'staticIPHostNameFQDN': 'string', 'displayCertificatesRenewalMessages': True}, 'acl': 'string', 'trackMovement': True, 'agentlessPosture': True, 'serviceTemplate': True, 'easywiredSessionCandidate': True, 'daclName': 'string', 'voiceDomainPermission': True, 'neat': True, 'webAuth': True, 'autoSmartPort': 'string', 'interfaceTemplate': 'string', 'ipv6ACLFilter': 'string', 'avcProfile': 'string', 'macSecPolicy': 'string', 'asaVpn': 'string', 'profileName': 'string', 'ipv6DaclName': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_AUTHORIZATION_PROFILE_9cb9f26e93655e7d89995b172f6fd97f(self):
        return re.search(
            self.AUTHORIZATION_PROFILE_9cb9f26e93655e7d89995b172f6fd97f_PATTERN,
            self.path
        )

    def authorization_profile_update_authorization_profile_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_AUTHORIZATION_PROFILE_c3913dfbda305f678ede16f782762ad3(self):
        return re.search(
            self.AUTHORIZATION_PROFILE_c3913dfbda305f678ede16f782762ad3_PATTERN,
            self.path
        )

    def authorization_profile_delete_authorization_profile_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_AUTHORIZATION_PROFILE_2e232c5666ab5ed783588f413c3bc644(self):
        return re.search(
            self.AUTHORIZATION_PROFILE_2e232c5666ab5ed783588f413c3bc644_PATTERN,
            self.path
        )

    def authorization_profile_get_all_authorization_profiles_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_AUTHORIZATION_PROFILE_9c43118f80d4556a8ec759a8c41e2097(self):
        return re.search(
            self.AUTHORIZATION_PROFILE_9c43118f80d4556a8ec759a8c41e2097_PATTERN,
            self.path
        )

    def authorization_profile_create_authorization_profile_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_AUTHORIZATION_PROFILE_3bee8aa3a03a57a3a5eb1418fe1250b6(self):
        return re.search(
            self.AUTHORIZATION_PROFILE_3bee8aa3a03a57a3a5eb1418fe1250b6_PATTERN,
            self.path
        )

    def authorization_profile_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_BYOD_PORTAL_effdf30a3e3a5781ba1f5cf833395359(self):
        return re.search(
            self.BYOD_PORTAL_effdf30a3e3a5781ba1f5cf833395359_PATTERN,
            self.path
        )

    def byod_portal_get_byod_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'BYODPortal': {'id': 'string', 'name': 'string', 'description': 'string', 'portalType': 'string', 'portalTestUrl': 'string', 'settings': {'portalSettings': {'httpsPort': 0, 'allowedInterfaces': ['string'], 'certificateGroupTag': 'string', 'endpointIdentityGroup': 'string', 'displayLang': 'string', 'fallbackLanguage': 'string', 'alwaysUsedLanguage': 'string'}, 'byodSettings': {'byodWelcomeSettings': {'enableBYOD': True, 'enableGuestAccess': True, 'requireMDM': True, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'requireScrolling': True}, 'byodRegistrationSettings': {'showDeviceID': True, 'endPointIdentityGroupId': 'string'}, 'byodRegistrationSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string', 'defaultEmptyFieldValue': 'string'}}, 'customizations': {'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'backgroundImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_BYOD_PORTAL_3e38d10b1ea257d49ebce893e87b3419(self):
        return re.search(
            self.BYOD_PORTAL_3e38d10b1ea257d49ebce893e87b3419_PATTERN,
            self.path
        )

    def byod_portal_update_byod_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_BYOD_PORTAL_df2fb34fbab65254ac87d1be50abd15f(self):
        return re.search(
            self.BYOD_PORTAL_df2fb34fbab65254ac87d1be50abd15f_PATTERN,
            self.path
        )

    def byod_portal_delete_byod_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_BYOD_PORTAL_41a23b580495514394b125800e073c9a(self):
        return re.search(
            self.BYOD_PORTAL_41a23b580495514394b125800e073c9a_PATTERN,
            self.path
        )

    def byod_portal_get_all_byod_portal_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_BYOD_PORTAL_afcce33ec863567f94f3b9b73719ff8d(self):
        return re.search(
            self.BYOD_PORTAL_afcce33ec863567f94f3b9b73719ff8d_PATTERN,
            self.path
        )

    def byod_portal_create_byod_portal_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_BYOD_PORTAL_c5d2d9d8c20b58049cd3326850f2292f(self):
        return re.search(
            self.BYOD_PORTAL_c5d2d9d8c20b58049cd3326850f2292f_PATTERN,
            self.path
        )

    def byod_portal_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATE_PROFILE_1d473b3690e951be9375d770225b9657(self):
        return re.search(
            self.CERTIFICATE_PROFILE_1d473b3690e951be9375d770225b9657_PATTERN,
            self.path
        )

    def certificate_profile_get_certificate_profile_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'CertificateProfile': {'id': 'string', 'name': 'string', 'description': 'string', 'externalIdentityStoreName': 'string', 'certificateAttributeName': 'string', 'allowedAsUserName': True, 'matchMode': 'string', 'usernameFrom': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATE_PROFILE_d24a3f485ff758d099b1e4713f18f1c1(self):
        return re.search(
            self.CERTIFICATE_PROFILE_d24a3f485ff758d099b1e4713f18f1c1_PATTERN,
            self.path
        )

    def certificate_profile_get_certificate_profile_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'CertificateProfile': {'id': 'string', 'name': 'string', 'description': 'string', 'externalIdentityStoreName': 'string', 'certificateAttributeName': 'string', 'allowedAsUserName': True, 'matchMode': 'string', 'usernameFrom': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATE_PROFILE_e09287aba99c56a6a9171b7e3a635a43(self):
        return re.search(
            self.CERTIFICATE_PROFILE_e09287aba99c56a6a9171b7e3a635a43_PATTERN,
            self.path
        )

    def certificate_profile_update_certificate_profile_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': [{'field': 'string', 'oldValue': 'string', 'newValue': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATE_PROFILE_3be38700993b5f70acfdc8e44f5558d8(self):
        return re.search(
            self.CERTIFICATE_PROFILE_3be38700993b5f70acfdc8e44f5558d8_PATTERN,
            self.path
        )

    def certificate_profile_get_all_certificate_profile_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATE_PROFILE_776141419f955525b0b38a57a3bed311(self):
        return re.search(
            self.CERTIFICATE_PROFILE_776141419f955525b0b38a57a3bed311_PATTERN,
            self.path
        )

    def certificate_profile_create_certificate_profile_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATE_PROFILE_8e00be3b97b85829bef60c09eaa922ac(self):
        return re.search(
            self.CERTIFICATE_PROFILE_8e00be3b97b85829bef60c09eaa922ac_PATTERN,
            self.path
        )

    def certificate_profile_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATE_TEMPLATE_e04f248274ea584aa30857975a28297f(self):
        return re.search(
            self.CERTIFICATE_TEMPLATE_e04f248274ea584aa30857975a28297f_PATTERN,
            self.path
        )

    def certificate_template_get_certificate_template_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSCertificateTemplate': {'id': 'string', 'name': 'string', 'description': 'string', 'keySize': 0, 'validityPeriod': 0, 'raprofile': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATE_TEMPLATE_e9e38cdf5bcb5c018b7f10f1d0864215(self):
        return re.search(
            self.CERTIFICATE_TEMPLATE_e9e38cdf5bcb5c018b7f10f1d0864215_PATTERN,
            self.path
        )

    def certificate_template_get_certificate_template_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSCertificateTemplate': {'id': 'string', 'name': 'string', 'description': 'string', 'keySize': 0, 'validityPeriod': 0, 'raprofile': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATE_TEMPLATE_dc1da5c3912a5117878160e27f6b533a(self):
        return re.search(
            self.CERTIFICATE_TEMPLATE_dc1da5c3912a5117878160e27f6b533a_PATTERN,
            self.path
        )

    def certificate_template_get_all_certificate_template_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CERTIFICATE_TEMPLATE_3f126f916efd575dbc9acae4ab2a1e4e(self):
        return re.search(
            self.CERTIFICATE_TEMPLATE_3f126f916efd575dbc9acae4ab2a1e4e_PATTERN,
            self.path
        )

    def certificate_template_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DOWNLOADABLE_ACL_dfa8f48210e85715beebb44e62fac408(self):
        return re.search(
            self.DOWNLOADABLE_ACL_dfa8f48210e85715beebb44e62fac408_PATTERN,
            self.path
        )

    def downloadable_acl_get_downloadable_acl_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'DownloadableAcl': {'id': 'string', 'name': 'string', 'description': 'string', 'dacl': 'string', 'daclType': 'string', 'link1': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DOWNLOADABLE_ACL_2d8c7ba0cb8f56d99135e16d2d973d11(self):
        return re.search(
            self.DOWNLOADABLE_ACL_2d8c7ba0cb8f56d99135e16d2d973d11_PATTERN,
            self.path
        )

    def downloadable_acl_update_downloadable_acl_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DOWNLOADABLE_ACL_42b3db444eaa50678218c29f88de60e8(self):
        return re.search(
            self.DOWNLOADABLE_ACL_42b3db444eaa50678218c29f88de60e8_PATTERN,
            self.path
        )

    def downloadable_acl_delete_downloadable_acl_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DOWNLOADABLE_ACL_9191bc200af85d598885a990ff9bcbf8(self):
        return re.search(
            self.DOWNLOADABLE_ACL_9191bc200af85d598885a990ff9bcbf8_PATTERN,
            self.path
        )

    def downloadable_acl_get_all_downloadable_acl_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DOWNLOADABLE_ACL_adcf947c42fe5588b7b82d9c43a3bbf0(self):
        return re.search(
            self.DOWNLOADABLE_ACL_adcf947c42fe5588b7b82d9c43a3bbf0_PATTERN,
            self.path
        )

    def downloadable_acl_create_downloadable_acl_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_DOWNLOADABLE_ACL_d10b7914625e5da0861cbeab4cf6440e(self):
        return re.search(
            self.DOWNLOADABLE_ACL_d10b7914625e5da0861cbeab4cf6440e_PATTERN,
            self.path
        )

    def downloadable_acl_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EGRESS_MATRIX_CELL_247716f503ab54e2921d713ed88f51c9(self):
        return re.search(
            self.EGRESS_MATRIX_CELL_247716f503ab54e2921d713ed88f51c9_PATTERN,
            self.path
        )

    def egress_matrix_cell_clear_all_matrix_cells_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EGRESS_MATRIX_CELL_90540642f47f525dbd71ef49710ef578(self):
        return re.search(
            self.EGRESS_MATRIX_CELL_90540642f47f525dbd71ef49710ef578_PATTERN,
            self.path
        )

    def egress_matrix_cell_set_all_cells_status_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EGRESS_MATRIX_CELL_892a1e6c05d05e67906b3b59bbe6d274(self):
        return re.search(
            self.EGRESS_MATRIX_CELL_892a1e6c05d05e67906b3b59bbe6d274_PATTERN,
            self.path
        )

    def egress_matrix_cell_clone_matrix_cell_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'OperationResult': {'resultValue': [{'value': 'string', 'name': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EGRESS_MATRIX_CELL_0cdc971b23285b87945021bd5983d1cd(self):
        return re.search(
            self.EGRESS_MATRIX_CELL_0cdc971b23285b87945021bd5983d1cd_PATTERN,
            self.path
        )

    def egress_matrix_cell_get_egress_matrix_cell_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'EgressMatrixCell': {'id': 'string', 'name': 'string', 'description': 'string', 'sourceSgtId': 'string', 'destinationSgtId': 'string', 'matrixCellStatus': 'string', 'defaultRule': 'string', 'sgacls': ['string'], 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EGRESS_MATRIX_CELL_ce83fba942c25938bae0c7012df68317(self):
        return re.search(
            self.EGRESS_MATRIX_CELL_ce83fba942c25938bae0c7012df68317_PATTERN,
            self.path
        )

    def egress_matrix_cell_update_egress_matrix_cell_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EGRESS_MATRIX_CELL_e4393915121d5bcc94dfde6c8f6f7f1c(self):
        return re.search(
            self.EGRESS_MATRIX_CELL_e4393915121d5bcc94dfde6c8f6f7f1c_PATTERN,
            self.path
        )

    def egress_matrix_cell_delete_egress_matrix_cell_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EGRESS_MATRIX_CELL_c5e52706e7095a81b8d32f3024e01cf6(self):
        return re.search(
            self.EGRESS_MATRIX_CELL_c5e52706e7095a81b8d32f3024e01cf6_PATTERN,
            self.path
        )

    def egress_matrix_cell_get_all_egress_matrix_cell_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EGRESS_MATRIX_CELL_64c560004d8b5f64a10f2cc070368c12(self):
        return re.search(
            self.EGRESS_MATRIX_CELL_64c560004d8b5f64a10f2cc070368c12_PATTERN,
            self.path
        )

    def egress_matrix_cell_create_egress_matrix_cell_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EGRESS_MATRIX_CELL_703c9da5c04b59358ac8bb1034340df4(self):
        return re.search(
            self.EGRESS_MATRIX_CELL_703c9da5c04b59358ac8bb1034340df4_PATTERN,
            self.path
        )

    def egress_matrix_cell_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EGRESS_MATRIX_CELL_aa333658bf83576eb36a025283516518(self):
        return re.search(
            self.EGRESS_MATRIX_CELL_aa333658bf83576eb36a025283516518_PATTERN,
            self.path
        )

    def egress_matrix_cell_bulk_request_for_egress_matrix_cell_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EGRESS_MATRIX_CELL_72048face30e52b28c76c1b2574de858(self):
        return re.search(
            self.EGRESS_MATRIX_CELL_72048face30e52b28c76c1b2574de858_PATTERN,
            self.path
        )

    def egress_matrix_cell_monitor_bulk_status_egress_matrix_cell_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'BulkStatus': {'bulkId': 'string', 'mediaType': 'string', 'executionStatus': 'string', 'operationType': 'string', 'startTime': 'string', 'resourcesCount': 0, 'successCount': 0, 'failCount': 0, 'resourcesStatus': [{'id': 'string', 'name': 'string', 'description': 'string', 'resourceExecutionStatus': 'string', 'status': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_CERTIFICATE_8e27d5df9cbe5b29a7e16bb7c877a4ce(self):
        return re.search(
            self.ENDPOINT_CERTIFICATE_8e27d5df9cbe5b29a7e16bb7c877a4ce_PATTERN,
            self.path
        )

    def endpoint_certificate_create_endpoint_certificate_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_CERTIFICATE_4c5c84028d8f5c078d8ab37553812d39(self):
        return re.search(
            self.ENDPOINT_CERTIFICATE_4c5c84028d8f5c078d8ab37553812d39_PATTERN,
            self.path
        )

    def endpoint_certificate_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_IDENTITY_GROUP_2590f64c3c08518e9eef83a92d69cde3(self):
        return re.search(
            self.ENDPOINT_IDENTITY_GROUP_2590f64c3c08518e9eef83a92d69cde3_PATTERN,
            self.path
        )

    def endpoint_identity_group_get_endpoint_group_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'EndPointGroup': {'id': 'string', 'name': 'string', 'description': 'string', 'systemDefined': True, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_IDENTITY_GROUP_5e4bfa620f76545d9887045cd24d99a2(self):
        return re.search(
            self.ENDPOINT_IDENTITY_GROUP_5e4bfa620f76545d9887045cd24d99a2_PATTERN,
            self.path
        )

    def endpoint_identity_group_get_endpoint_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'EndPointGroup': {'id': 'string', 'name': 'string', 'description': 'string', 'systemDefined': True, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_IDENTITY_GROUP_189979b4e8d45639975c226dacd53e7b(self):
        return re.search(
            self.ENDPOINT_IDENTITY_GROUP_189979b4e8d45639975c226dacd53e7b_PATTERN,
            self.path
        )

    def endpoint_identity_group_update_endpoint_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_IDENTITY_GROUP_f7b0aab2a65652feae637779bfb20d2d(self):
        return re.search(
            self.ENDPOINT_IDENTITY_GROUP_f7b0aab2a65652feae637779bfb20d2d_PATTERN,
            self.path
        )

    def endpoint_identity_group_delete_endpoint_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_IDENTITY_GROUP_cd429bb8ff3556a796570480f742028b(self):
        return re.search(
            self.ENDPOINT_IDENTITY_GROUP_cd429bb8ff3556a796570480f742028b_PATTERN,
            self.path
        )

    def endpoint_identity_group_get_all_endpoint_groups_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_IDENTITY_GROUP_b14d63c641e95ac0a8c2da2fb65909c7(self):
        return re.search(
            self.ENDPOINT_IDENTITY_GROUP_b14d63c641e95ac0a8c2da2fb65909c7_PATTERN,
            self.path
        )

    def endpoint_identity_group_create_endpoint_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_IDENTITY_GROUP_1d553cc3b48d5689ac45a582a5d98f9b(self):
        return re.search(
            self.ENDPOINT_IDENTITY_GROUP_1d553cc3b48d5689ac45a582a5d98f9b_PATTERN,
            self.path
        )

    def endpoint_identity_group_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_258969f4f97557daacb3dadaced526cc(self):
        return re.search(
            self.ENDPOINT_258969f4f97557daacb3dadaced526cc_PATTERN,
            self.path
        )

    def endpoint_release_rejected_endpoint_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_ed121b2686e85bd5b28c068c3c0de220(self):
        return re.search(
            self.ENDPOINT_ed121b2686e85bd5b28c068c3c0de220_PATTERN,
            self.path
        )

    def endpoint_deregister_endpoint_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_f8a2f0834e625822bed1cb4cf34fde5e(self):
        return re.search(
            self.ENDPOINT_f8a2f0834e625822bed1cb4cf34fde5e_PATTERN,
            self.path
        )

    def endpoint_get_rejected_endpoints_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'OperationResult': {'resultValue': [{'value': 'string', 'name': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_7d53842e83f0538cab91e097aa6800ce(self):
        return re.search(
            self.ENDPOINT_7d53842e83f0538cab91e097aa6800ce_PATTERN,
            self.path
        )

    def endpoint_get_endpoint_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSEndPoint': {'id': 'string', 'name': 'string', 'description': 'string', 'mac': 'string', 'profileId': 'string', 'staticProfileAssignment': True, 'groupId': 'string', 'staticGroupAssignment': True, 'portalUser': 'string', 'identityStore': 'string', 'identityStoreId': 'string', 'customAttributes': {'customAttributes': {}}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_eb8e0ce63376573995a49178435f7747(self):
        return re.search(
            self.ENDPOINT_eb8e0ce63376573995a49178435f7747_PATTERN,
            self.path
        )

    def endpoint_get_endpoint_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSEndPoint': {'id': 'string', 'name': 'string', 'description': 'string', 'mac': 'string', 'profileId': 'string', 'staticProfileAssignment': True, 'groupId': 'string', 'staticGroupAssignment': True, 'portalUser': 'string', 'identityStore': 'string', 'identityStoreId': 'string', 'customAttributes': {'customAttributes': {}}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_c8b30af4b84b5a90be2fc152cf26ad42(self):
        return re.search(
            self.ENDPOINT_c8b30af4b84b5a90be2fc152cf26ad42_PATTERN,
            self.path
        )

    def endpoint_update_endpoint_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_36658f1cac5f578ab6509196266ad8e3(self):
        return re.search(
            self.ENDPOINT_36658f1cac5f578ab6509196266ad8e3_PATTERN,
            self.path
        )

    def endpoint_delete_endpoint_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_dfaeea899c185169ae2a3b70b5491008(self):
        return re.search(
            self.ENDPOINT_dfaeea899c185169ae2a3b70b5491008_PATTERN,
            self.path
        )

    def endpoint_register_endpoint_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_719765b7f7285d71be4645db91b0fc74(self):
        return re.search(
            self.ENDPOINT_719765b7f7285d71be4645db91b0fc74_PATTERN,
            self.path
        )

    def endpoint_get_all_endpoints_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_845787ab88be5092bf4ba9f522e8e26f(self):
        return re.search(
            self.ENDPOINT_845787ab88be5092bf4ba9f522e8e26f_PATTERN,
            self.path
        )

    def endpoint_create_endpoint_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_85adcb1d998d54838add3b4d644242af(self):
        return re.search(
            self.ENDPOINT_85adcb1d998d54838add3b4d644242af_PATTERN,
            self.path
        )

    def endpoint_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_c03505504e8e5af8a715e27c40f16eab(self):
        return re.search(
            self.ENDPOINT_c03505504e8e5af8a715e27c40f16eab_PATTERN,
            self.path
        )

    def endpoint_bulk_request_for_endpoint_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_ENDPOINT_5b054a43ba875f0da3da5a7d863f3ef7(self):
        return re.search(
            self.ENDPOINT_5b054a43ba875f0da3da5a7d863f3ef7_PATTERN,
            self.path
        )

    def endpoint_monitor_bulk_status_endpoint_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'BulkStatus': {'bulkId': 'string', 'mediaType': 'string', 'executionStatus': 'string', 'operationType': 'string', 'startTime': 'string', 'resourcesCount': 0, 'successCount': 0, 'failCount': 0, 'resourcesStatus': [{'id': 'string', 'name': 'string', 'description': 'string', 'resourceExecutionStatus': 'string', 'status': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EXTERNAL_RADIUS_SERVER_e6019b6b2b605132b57db142f581e710(self):
        return re.search(
            self.EXTERNAL_RADIUS_SERVER_e6019b6b2b605132b57db142f581e710_PATTERN,
            self.path
        )

    def external_radius_server_get_external_radius_server_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ExternalRadiusServer': {'id': 'string', 'name': 'string', 'description': 'string', 'hostIP': 'string', 'sharedSecret': 'string', 'enableKeyWrap': True, 'encryptionKey': 'string', 'authenticatorKey': 'string', 'keyInputFormat': 'string', 'authenticationPort': 0, 'accountingPort': 0, 'timeout': 0, 'retries': 0, 'proxyTimeout': 0, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EXTERNAL_RADIUS_SERVER_81735151a93c51c59037ec968625ee45(self):
        return re.search(
            self.EXTERNAL_RADIUS_SERVER_81735151a93c51c59037ec968625ee45_PATTERN,
            self.path
        )

    def external_radius_server_get_external_radius_server_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ExternalRadiusServer': {'id': 'string', 'name': 'string', 'description': 'string', 'hostIP': 'string', 'sharedSecret': 'string', 'enableKeyWrap': True, 'encryptionKey': 'string', 'authenticatorKey': 'string', 'keyInputFormat': 'string', 'authenticationPort': 0, 'accountingPort': 0, 'timeout': 0, 'retries': 0, 'proxyTimeout': 0, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EXTERNAL_RADIUS_SERVER_28036825e94f5eba9d9615a3ecc18ebc(self):
        return re.search(
            self.EXTERNAL_RADIUS_SERVER_28036825e94f5eba9d9615a3ecc18ebc_PATTERN,
            self.path
        )

    def external_radius_server_update_external_radius_server_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EXTERNAL_RADIUS_SERVER_373fcbde1c215f95bebbfa95780ed9a8(self):
        return re.search(
            self.EXTERNAL_RADIUS_SERVER_373fcbde1c215f95bebbfa95780ed9a8_PATTERN,
            self.path
        )

    def external_radius_server_delete_external_radius_server_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EXTERNAL_RADIUS_SERVER_9b641825a9555ecba105cabbdf50fc78(self):
        return re.search(
            self.EXTERNAL_RADIUS_SERVER_9b641825a9555ecba105cabbdf50fc78_PATTERN,
            self.path
        )

    def external_radius_server_get_all_external_radius_server_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EXTERNAL_RADIUS_SERVER_1fc1c74b35ae5050b4f7fd702570ad5b(self):
        return re.search(
            self.EXTERNAL_RADIUS_SERVER_1fc1c74b35ae5050b4f7fd702570ad5b_PATTERN,
            self.path
        )

    def external_radius_server_create_external_radius_server_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_EXTERNAL_RADIUS_SERVER_a6c3ffe72746500b88be3a5418ead4ba(self):
        return re.search(
            self.EXTERNAL_RADIUS_SERVER_a6c3ffe72746500b88be3a5418ead4ba_PATTERN,
            self.path
        )

    def external_radius_server_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_FILTER_POLICY_16555f5d5ab6568d8bf5f9932f7ed7f4(self):
        return re.search(
            self.FILTER_POLICY_16555f5d5ab6568d8bf5f9932f7ed7f4_PATTERN,
            self.path
        )

    def filter_policy_get_filter_policy_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSFilterPolicy': {'subnet': 'string', 'domains': 'string', 'sgt': 'string', 'vn': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_FILTER_POLICY_95d0006cc03d53c89a3593526bf8dc0f(self):
        return re.search(
            self.FILTER_POLICY_95d0006cc03d53c89a3593526bf8dc0f_PATTERN,
            self.path
        )

    def filter_policy_update_filter_policy_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_FILTER_POLICY_4a83e0d4f56a5c06946f685aa46fa3e3(self):
        return re.search(
            self.FILTER_POLICY_4a83e0d4f56a5c06946f685aa46fa3e3_PATTERN,
            self.path
        )

    def filter_policy_delete_filter_policy_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_FILTER_POLICY_250a599ae00f5e47b9ece23cd3183d1c(self):
        return re.search(
            self.FILTER_POLICY_250a599ae00f5e47b9ece23cd3183d1c_PATTERN,
            self.path
        )

    def filter_policy_get_all_filter_policy_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_FILTER_POLICY_22f8082b07ce528f82545e210b84d7de(self):
        return re.search(
            self.FILTER_POLICY_22f8082b07ce528f82545e210b84d7de_PATTERN,
            self.path
        )

    def filter_policy_create_filter_policy_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_FILTER_POLICY_209810ed6cad570d90243b1e0dbbe27b(self):
        return re.search(
            self.FILTER_POLICY_209810ed6cad570d90243b1e0dbbe27b_PATTERN,
            self.path
        )

    def filter_policy_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_LOCATION_ca2e75fbf5b45ba3b399e5616458b855(self):
        return re.search(
            self.GUEST_LOCATION_ca2e75fbf5b45ba3b399e5616458b855_PATTERN,
            self.path
        )

    def guest_location_get_guest_location_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'LocationIdentification': {'id': 'string', 'name': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_LOCATION_13ea10f18c3655db84657ad855bf6972(self):
        return re.search(
            self.GUEST_LOCATION_13ea10f18c3655db84657ad855bf6972_PATTERN,
            self.path
        )

    def guest_location_get_all_guest_location_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_LOCATION_fdfe562af248561f981549b96f8ed397(self):
        return re.search(
            self.GUEST_LOCATION_fdfe562af248561f981549b96f8ed397_PATTERN,
            self.path
        )

    def guest_location_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_SMTP_NOTIFICATION_CONFIGURATION_ca28129793d1569bb50de9f43b0d0ee8(self):
        return re.search(
            self.GUEST_SMTP_NOTIFICATION_CONFIGURATION_ca28129793d1569bb50de9f43b0d0ee8_PATTERN,
            self.path
        )

    def guest_smtp_notification_configuration_get_guest_smtp_notification_settings_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSGuestSmtpNotificationSettings': {'id': 'string', 'smtpServer': 'string', 'notificationEnabled': True, 'useDefaultFromAddress': True, 'defaultFromAddress': 'string', 'smtpPort': 'string', 'connectionTimeout': 'string', 'useTLSorSSLEncryption': True, 'usePasswordAuthentication': True, 'userName': 'string', 'password': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_SMTP_NOTIFICATION_CONFIGURATION_a7500f6e473a50e19452683e303dd021(self):
        return re.search(
            self.GUEST_SMTP_NOTIFICATION_CONFIGURATION_a7500f6e473a50e19452683e303dd021_PATTERN,
            self.path
        )

    def guest_smtp_notification_configuration_update_guest_smtp_notification_settings_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_SMTP_NOTIFICATION_CONFIGURATION_51e4c74e9b4e559e95c73e81183a6c7a(self):
        return re.search(
            self.GUEST_SMTP_NOTIFICATION_CONFIGURATION_51e4c74e9b4e559e95c73e81183a6c7a_PATTERN,
            self.path
        )

    def guest_smtp_notification_configuration_get_all_guest_smtp_notification_settings_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_SMTP_NOTIFICATION_CONFIGURATION_01643de7c6f75f68b0d7df00dc72808d(self):
        return re.search(
            self.GUEST_SMTP_NOTIFICATION_CONFIGURATION_01643de7c6f75f68b0d7df00dc72808d_PATTERN,
            self.path
        )

    def guest_smtp_notification_configuration_create_guest_smtp_notification_settings_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_SMTP_NOTIFICATION_CONFIGURATION_0a0c0e67aead55a2b4db67e9d068351a(self):
        return re.search(
            self.GUEST_SMTP_NOTIFICATION_CONFIGURATION_0a0c0e67aead55a2b4db67e9d068351a_PATTERN,
            self.path
        )

    def guest_smtp_notification_configuration_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_SSID_d5572c56526151cb8ea42de44b2db52c(self):
        return re.search(
            self.GUEST_SSID_d5572c56526151cb8ea42de44b2db52c_PATTERN,
            self.path
        )

    def guest_ssid_get_guest_ssid_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'GuestSSID': {'id': 'string', 'name': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_SSID_72e6e4b7d022556a80f1948efb3d5c61(self):
        return re.search(
            self.GUEST_SSID_72e6e4b7d022556a80f1948efb3d5c61_PATTERN,
            self.path
        )

    def guest_ssid_update_guest_ssid_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_SSID_8328407df7345f788230a512d6635c25(self):
        return re.search(
            self.GUEST_SSID_8328407df7345f788230a512d6635c25_PATTERN,
            self.path
        )

    def guest_ssid_delete_guest_ssid_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_SSID_c37778a2faa5552894cc60cec13c56c7(self):
        return re.search(
            self.GUEST_SSID_c37778a2faa5552894cc60cec13c56c7_PATTERN,
            self.path
        )

    def guest_ssid_get_all_guest_ssid_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_SSID_2a31eb33e3535754b3f754a9199e0d25(self):
        return re.search(
            self.GUEST_SSID_2a31eb33e3535754b3f754a9199e0d25_PATTERN,
            self.path
        )

    def guest_ssid_create_guest_ssid_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_SSID_b400ebaa2d1f51398d3b32e7a6e4ba35(self):
        return re.search(
            self.GUEST_SSID_b400ebaa2d1f51398d3b32e7a6e4ba35_PATTERN,
            self.path
        )

    def guest_ssid_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_TYPE_01c7aed7320e54bfac29f13c8717a6b5(self):
        return re.search(
            self.GUEST_TYPE_01c7aed7320e54bfac29f13c8717a6b5_PATTERN,
            self.path
        )

    def guest_type_update_guest_type_email_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_TYPE_f9661f7c85c2570897cffc3d02668263(self):
        return re.search(
            self.GUEST_TYPE_f9661f7c85c2570897cffc3d02668263_PATTERN,
            self.path
        )

    def guest_type_update_guest_type_sms_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_TYPE_4acb5a41fe395b158a3fe1cda996b0cf(self):
        return re.search(
            self.GUEST_TYPE_4acb5a41fe395b158a3fe1cda996b0cf_PATTERN,
            self.path
        )

    def guest_type_get_guest_type_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'GuestType': {'id': 'string', 'name': 'string', 'description': 'string', 'isDefaultType': True, 'accessTime': {'fromFirstLogin': True, 'maxAccountDuration': 0, 'durationTimeUnit': 'string', 'defaultDuration': 0, 'allowAccessOnSpecificDaysTimes': True, 'dayTimeLimits': [{'startTime': 'string', 'endTime': 'string', 'days': ['string']}]}, 'loginOptions': {'limitSimultaneousLogins': True, 'maxSimultaneousLogins': 0, 'failureAction': 'string', 'maxRegisteredDevices': 0, 'identityGroupId': 'string', 'allowGuestPortalBypass': True}, 'expirationNotification': {'enableNotification': True, 'advanceNotificationDuration': 0, 'advanceNotificationUnits': 'string', 'sendEmailNotification': True, 'emailText': 'string', 'sendSmsNotification': True, 'smsText': 'string'}, 'sponsorGroups': ['string'], 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_TYPE_bac6d4d95ac45a0a8933b8712dcbe70d(self):
        return re.search(
            self.GUEST_TYPE_bac6d4d95ac45a0a8933b8712dcbe70d_PATTERN,
            self.path
        )

    def guest_type_update_guest_type_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_TYPE_6faa7211d68e5b329034e17c82b78694(self):
        return re.search(
            self.GUEST_TYPE_6faa7211d68e5b329034e17c82b78694_PATTERN,
            self.path
        )

    def guest_type_delete_guest_type_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_TYPE_0f41a1e47105581fabf212f259626903(self):
        return re.search(
            self.GUEST_TYPE_0f41a1e47105581fabf212f259626903_PATTERN,
            self.path
        )

    def guest_type_get_all_guest_type_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_TYPE_f46c01449d585b088490c4db530c56d5(self):
        return re.search(
            self.GUEST_TYPE_f46c01449d585b088490c4db530c56d5_PATTERN,
            self.path
        )

    def guest_type_create_guest_type_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_TYPE_a6bfaedfca185fb7b6a86621e866a5f6(self):
        return re.search(
            self.GUEST_TYPE_a6bfaedfca185fb7b6a86621e866a5f6_PATTERN,
            self.path
        )

    def guest_type_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_c67b4dcffba052ae8ece775bc61a1c21(self):
        return re.search(
            self.GUEST_USER_c67b4dcffba052ae8ece775bc61a1c21_PATTERN,
            self.path
        )

    def guest_user_approve_guest_user_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_2eb3472c4de150828b2dae61e2285313(self):
        return re.search(
            self.GUEST_USER_2eb3472c4de150828b2dae61e2285313_PATTERN,
            self.path
        )

    def guest_user_change_sponsor_password_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_83983afcc8fe53b4824ae744a2ff3848(self):
        return re.search(
            self.GUEST_USER_83983afcc8fe53b4824ae744a2ff3848_PATTERN,
            self.path
        )

    def guest_user_suspend_guest_user_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_18b21045846d5097a82cd61cb3c7eaf1(self):
        return re.search(
            self.GUEST_USER_18b21045846d5097a82cd61cb3c7eaf1_PATTERN,
            self.path
        )

    def guest_user_reinstate_guest_user_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_bcb7ec29968e5d5899df4a90d94ed659(self):
        return re.search(
            self.GUEST_USER_bcb7ec29968e5d5899df4a90d94ed659_PATTERN,
            self.path
        )

    def guest_user_get_guest_user_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'GuestUser': {'id': 'string', 'name': 'string', 'description': 'string', 'guestType': 'string', 'status': 'string', 'statusReason': 'string', 'reasonForVisit': 'string', 'sponsorUserId': 'string', 'sponsorUserName': 'string', 'guestInfo': {'firstName': 'string', 'lastName': 'string', 'company': 'string', 'creationTime': 'string', 'notificationLanguage': 'string', 'userName': 'string', 'emailAddress': 'string', 'phoneNumber': 'string', 'password': 'string', 'enabled': True, 'smsServiceProvider': 'string'}, 'guestAccessInfo': {'validDays': 0, 'fromDate': 'string', 'toDate': 'string', 'location': 'string', 'ssid': 'string', 'groupTag': 'string'}, 'portalId': 'string', 'customFields': {}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_f24049df29d059c48eef86d381ffad5d(self):
        return re.search(
            self.GUEST_USER_f24049df29d059c48eef86d381ffad5d_PATTERN,
            self.path
        )

    def guest_user_update_guest_user_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_76ef15d7c6b259f5859ee9675c38887c(self):
        return re.search(
            self.GUEST_USER_76ef15d7c6b259f5859ee9675c38887c_PATTERN,
            self.path
        )

    def guest_user_delete_guest_user_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_7ea6ea4e41d85f83b6f6c10ce38bb9ed(self):
        return re.search(
            self.GUEST_USER_7ea6ea4e41d85f83b6f6c10ce38bb9ed_PATTERN,
            self.path
        )

    def guest_user_reset_guest_user_password_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'OperationResult': {'resultValue': [{'value': 'string', 'name': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_4dfcba4a0f685c168bdf2b5b2be317ac(self):
        return re.search(
            self.GUEST_USER_4dfcba4a0f685c168bdf2b5b2be317ac_PATTERN,
            self.path
        )

    def guest_user_reinstate_guest_user_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_9a9fa9cbccbe50fcb1cd6a63fed47578(self):
        return re.search(
            self.GUEST_USER_9a9fa9cbccbe50fcb1cd6a63fed47578_PATTERN,
            self.path
        )

    def guest_user_update_guest_user_email_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_290601ba14b751f98206ca2e19cff3fe(self):
        return re.search(
            self.GUEST_USER_290601ba14b751f98206ca2e19cff3fe_PATTERN,
            self.path
        )

    def guest_user_update_guest_user_sms_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_3c1e5e2a187652018c59b10155ac973d(self):
        return re.search(
            self.GUEST_USER_3c1e5e2a187652018c59b10155ac973d_PATTERN,
            self.path
        )

    def guest_user_deny_guest_user_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_2645275c3c7d5a3a83d9f7441972d399(self):
        return re.search(
            self.GUEST_USER_2645275c3c7d5a3a83d9f7441972d399_PATTERN,
            self.path
        )

    def guest_user_get_guest_user_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'GuestUser': {'id': 'string', 'name': 'string', 'description': 'string', 'guestType': 'string', 'status': 'string', 'statusReason': 'string', 'reasonForVisit': 'string', 'sponsorUserId': 'string', 'sponsorUserName': 'string', 'guestInfo': {'firstName': 'string', 'lastName': 'string', 'company': 'string', 'creationTime': 'string', 'notificationLanguage': 'string', 'userName': 'string', 'emailAddress': 'string', 'phoneNumber': 'string', 'password': 'string', 'enabled': True, 'smsServiceProvider': 'string'}, 'guestAccessInfo': {'validDays': 0, 'fromDate': 'string', 'toDate': 'string', 'location': 'string', 'ssid': 'string', 'groupTag': 'string'}, 'portalId': 'string', 'customFields': {}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_8754551b9c7c5847b17684c49399ff95(self):
        return re.search(
            self.GUEST_USER_8754551b9c7c5847b17684c49399ff95_PATTERN,
            self.path
        )

    def guest_user_update_guest_user_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_1030e251b39f55d3ac2570a963a3ee9c(self):
        return re.search(
            self.GUEST_USER_1030e251b39f55d3ac2570a963a3ee9c_PATTERN,
            self.path
        )

    def guest_user_delete_guest_user_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_1a5abd33eeaa52e39e926472751ef79e(self):
        return re.search(
            self.GUEST_USER_1a5abd33eeaa52e39e926472751ef79e_PATTERN,
            self.path
        )

    def guest_user_get_all_guest_users_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_89f7cf06a1655d6da606ace9b0950bcf(self):
        return re.search(
            self.GUEST_USER_89f7cf06a1655d6da606ace9b0950bcf_PATTERN,
            self.path
        )

    def guest_user_create_guest_user_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_08be5b1e320e55f4a181370417471d9e(self):
        return re.search(
            self.GUEST_USER_08be5b1e320e55f4a181370417471d9e_PATTERN,
            self.path
        )

    def guest_user_suspend_guest_user_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_76abe22ea0c45f619731bd568c9f57f4(self):
        return re.search(
            self.GUEST_USER_76abe22ea0c45f619731bd568c9f57f4_PATTERN,
            self.path
        )

    def guest_user_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_37edfca30e8e514d9bab840c3c2d4c0f(self):
        return re.search(
            self.GUEST_USER_37edfca30e8e514d9bab840c3c2d4c0f_PATTERN,
            self.path
        )

    def guest_user_bulk_request_for_guest_user_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_GUEST_USER_e38a1af3ad835636a11375363528fa2e(self):
        return re.search(
            self.GUEST_USER_e38a1af3ad835636a11375363528fa2e_PATTERN,
            self.path
        )

    def guest_user_monitor_bulk_status_guest_user_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'BulkStatus': {'bulkId': 'string', 'mediaType': 'string', 'executionStatus': 'string', 'operationType': 'string', 'startTime': 'string', 'resourcesCount': 0, 'successCount': 0, 'failCount': 0, 'resourcesStatus': [{'id': 'string', 'name': 'string', 'description': 'string', 'resourceExecutionStatus': 'string', 'status': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_HOTSPOT_PORTAL_6cbcecf65a0155fcad602d3ac16531a7(self):
        return re.search(
            self.HOTSPOT_PORTAL_6cbcecf65a0155fcad602d3ac16531a7_PATTERN,
            self.path
        )

    def hotspot_portal_get_hotspot_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'HotspotPortal': {'id': 'string', 'name': 'string', 'description': 'string', 'portalType': 'string', 'portalTestUrl': 'string', 'settings': {'portalSettings': {'httpsPort': 0, 'allowedInterfaces': 'string', 'certificateGroupTag': 'string', 'endpointIdentityGroup': 'string', 'coaType': 'string', 'displayLang': 'string', 'fallbackLanguage': 'string', 'alwaysUsedLanguage': 'string'}, 'aupSettings': {'requireAccessCode': True, 'accessCode': 'string', 'includeAup': True, 'requireScrolling': True}, 'postAccessBannerSettings': {'includePostAccessBanner': True}, 'authSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string', 'defaultEmptyFieldValue': 'string'}}, 'customizations': {'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'backgroundImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_HOTSPOT_PORTAL_0ae4af25df565334b20a24c4878b68e4(self):
        return re.search(
            self.HOTSPOT_PORTAL_0ae4af25df565334b20a24c4878b68e4_PATTERN,
            self.path
        )

    def hotspot_portal_update_hotspot_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_HOTSPOT_PORTAL_1a344d1c6f535789b7badbaa502e8d3b(self):
        return re.search(
            self.HOTSPOT_PORTAL_1a344d1c6f535789b7badbaa502e8d3b_PATTERN,
            self.path
        )

    def hotspot_portal_delete_hotspot_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_HOTSPOT_PORTAL_d912b1c21e2b5dca8b56332d3a8ad13d(self):
        return re.search(
            self.HOTSPOT_PORTAL_d912b1c21e2b5dca8b56332d3a8ad13d_PATTERN,
            self.path
        )

    def hotspot_portal_get_all_hotspot_portal_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_HOTSPOT_PORTAL_0df78c9a3f72584dbd1c7b667b0e312f(self):
        return re.search(
            self.HOTSPOT_PORTAL_0df78c9a3f72584dbd1c7b667b0e312f_PATTERN,
            self.path
        )

    def hotspot_portal_create_hotspot_portal_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_HOTSPOT_PORTAL_91257d81be4f5a0486cc085499c19b1c(self):
        return re.search(
            self.HOTSPOT_PORTAL_91257d81be4f5a0486cc085499c19b1c_PATTERN,
            self.path
        )

    def hotspot_portal_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IDENTITY_GROUPS_1f18bdd1938755409bf6db6b29e85d3a(self):
        return re.search(
            self.IDENTITY_GROUPS_1f18bdd1938755409bf6db6b29e85d3a_PATTERN,
            self.path
        )

    def identity_groups_get_identity_group_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'IdentityGroup': {'id': 'string', 'name': 'string', 'description': 'string', 'parent': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IDENTITY_GROUPS_ca3df31c13b857e6b5dbc8357a8ab010(self):
        return re.search(
            self.IDENTITY_GROUPS_ca3df31c13b857e6b5dbc8357a8ab010_PATTERN,
            self.path
        )

    def identity_groups_get_identity_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'IdentityGroup': {'id': 'string', 'name': 'string', 'description': 'string', 'parent': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IDENTITY_GROUPS_1c0689e940ba5526946ad15976cc3365(self):
        return re.search(
            self.IDENTITY_GROUPS_1c0689e940ba5526946ad15976cc3365_PATTERN,
            self.path
        )

    def identity_groups_update_identity_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IDENTITY_GROUPS_9d904c521059563490c4a93871b33d51(self):
        return re.search(
            self.IDENTITY_GROUPS_9d904c521059563490c4a93871b33d51_PATTERN,
            self.path
        )

    def identity_groups_get_all_identity_groups_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IDENTITY_GROUPS_592250bf19f653f9a5c48d1fb1890409(self):
        return re.search(
            self.IDENTITY_GROUPS_592250bf19f653f9a5c48d1fb1890409_PATTERN,
            self.path
        )

    def identity_groups_create_identity_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IDENTITY_GROUPS_aab79aee0b455bfea8a6d7c6464a2a09(self):
        return re.search(
            self.IDENTITY_GROUPS_aab79aee0b455bfea8a6d7c6464a2a09_PATTERN,
            self.path
        )

    def identity_groups_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IDENTITY_SEQUENCE_db686413cf4558188ea60ccc05c3e920(self):
        return re.search(
            self.IDENTITY_SEQUENCE_db686413cf4558188ea60ccc05c3e920_PATTERN,
            self.path
        )

    def identity_sequence_get_identity_sequence_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'IdStoreSequence': {'id': 'string', 'name': 'string', 'description': 'string', 'idSeqItem': [{'idstore': 'string', 'order': 0}], 'certificateAuthenticationProfile': 'string', 'breakOnStoreFail': True, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IDENTITY_SEQUENCE_45cb9345e58f5433ae80f5d8f855978b(self):
        return re.search(
            self.IDENTITY_SEQUENCE_45cb9345e58f5433ae80f5d8f855978b_PATTERN,
            self.path
        )

    def identity_sequence_get_identity_sequence_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'IdStoreSequence': {'id': 'string', 'name': 'string', 'description': 'string', 'idSeqItem': [{'idstore': 'string', 'order': 0}], 'certificateAuthenticationProfile': 'string', 'breakOnStoreFail': True, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IDENTITY_SEQUENCE_9c316d5e2fdd51bdab039ea9e2a417bd(self):
        return re.search(
            self.IDENTITY_SEQUENCE_9c316d5e2fdd51bdab039ea9e2a417bd_PATTERN,
            self.path
        )

    def identity_sequence_update_identity_sequence_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IDENTITY_SEQUENCE_2b8258803668534d87781e995c73c23a(self):
        return re.search(
            self.IDENTITY_SEQUENCE_2b8258803668534d87781e995c73c23a_PATTERN,
            self.path
        )

    def identity_sequence_delete_identity_sequence_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IDENTITY_SEQUENCE_feb30ca768795eed82c118d009d7bcd4(self):
        return re.search(
            self.IDENTITY_SEQUENCE_feb30ca768795eed82c118d009d7bcd4_PATTERN,
            self.path
        )

    def identity_sequence_get_all_identity_sequence_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IDENTITY_SEQUENCE_6cc0a87094bf5d96af61403dfc3747db(self):
        return re.search(
            self.IDENTITY_SEQUENCE_6cc0a87094bf5d96af61403dfc3747db_PATTERN,
            self.path
        )

    def identity_sequence_create_identity_sequence_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IDENTITY_SEQUENCE_dc4c840ad93e53d591ca3a39184e6dde(self):
        return re.search(
            self.IDENTITY_SEQUENCE_dc4c840ad93e53d591ca3a39184e6dde_PATTERN,
            self.path
        )

    def identity_sequence_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_INTERNAL_USER_7f403dda9440503191536993f569cc6f(self):
        return re.search(
            self.INTERNAL_USER_7f403dda9440503191536993f569cc6f_PATTERN,
            self.path
        )

    def internal_user_get_internal_user_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'InternalUser': {'id': 'string', 'name': 'string', 'description': 'string', 'enabled': True, 'email': 'string', 'password': 'string', 'firstName': 'string', 'lastName': 'string', 'changePassword': True, 'identityGroups': 'string', 'expiryDateEnabled': True, 'expiryDate': 'string', 'enablePassword': 'string', 'customAttributes': {}, 'passwordIDStore': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_INTERNAL_USER_4758008519d9509db339e3b27dc56b37(self):
        return re.search(
            self.INTERNAL_USER_4758008519d9509db339e3b27dc56b37_PATTERN,
            self.path
        )

    def internal_user_update_internal_user_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_INTERNAL_USER_2447b4e2fc3e595aa1be86d6589614b9(self):
        return re.search(
            self.INTERNAL_USER_2447b4e2fc3e595aa1be86d6589614b9_PATTERN,
            self.path
        )

    def internal_user_delete_internal_user_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_INTERNAL_USER_bacf1abfc35e509183c9a7f055cbbfec(self):
        return re.search(
            self.INTERNAL_USER_bacf1abfc35e509183c9a7f055cbbfec_PATTERN,
            self.path
        )

    def internal_user_get_internal_user_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'InternalUser': {'id': 'string', 'name': 'string', 'description': 'string', 'enabled': True, 'email': 'string', 'password': 'string', 'firstName': 'string', 'lastName': 'string', 'changePassword': True, 'identityGroups': 'string', 'expiryDateEnabled': True, 'expiryDate': 'string', 'enablePassword': 'string', 'customAttributes': {}, 'passwordIDStore': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_INTERNAL_USER_f7227b280b745b94bb801369b168a529(self):
        return re.search(
            self.INTERNAL_USER_f7227b280b745b94bb801369b168a529_PATTERN,
            self.path
        )

    def internal_user_update_internal_user_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_INTERNAL_USER_dcf28db5184e51139b15f9ffccd10b67(self):
        return re.search(
            self.INTERNAL_USER_dcf28db5184e51139b15f9ffccd10b67_PATTERN,
            self.path
        )

    def internal_user_delete_internal_user_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_INTERNAL_USER_3ccba98a61555ae495f6a05284e3b5ae(self):
        return re.search(
            self.INTERNAL_USER_3ccba98a61555ae495f6a05284e3b5ae_PATTERN,
            self.path
        )

    def internal_user_get_all_internal_user_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_INTERNAL_USER_bf175c04fcb051b9a6fd70a2252903fa(self):
        return re.search(
            self.INTERNAL_USER_bf175c04fcb051b9a6fd70a2252903fa_PATTERN,
            self.path
        )

    def internal_user_create_internal_user_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_INTERNAL_USER_2af99828533e58a2b84996b85bacc9ff(self):
        return re.search(
            self.INTERNAL_USER_2af99828533e58a2b84996b85bacc9ff_PATTERN,
            self.path
        )

    def internal_user_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_GROUP_bd7f3fb27d71596ebafecca578c85bc7(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_GROUP_bd7f3fb27d71596ebafecca578c85bc7_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_group_deploy_ip_to_sgt_mapping_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_GROUP_0b8ef94d6d5554a4b57d37c52612ad7d(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_GROUP_0b8ef94d6d5554a4b57d37c52612ad7d_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_group_deploy_all_ip_to_sgt_mapping_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_GROUP_d6c25690e3a854c5be7763a4106e379e(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_GROUP_d6c25690e3a854c5be7763a4106e379e_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_group_get_deploy_status_ip_to_sgt_mapping_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'OperationResult': {'resultValue': [{'value': 'string', 'name': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_GROUP_e56b94dafa5652228fd71abd2b4d6df3(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_GROUP_e56b94dafa5652228fd71abd2b4d6df3_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_group_get_ip_to_sgt_mapping_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SGMappingGroup': {'name': 'string', 'sgt': 'string', 'deployTo': 'string', 'deployType': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_GROUP_02a5a26c964e53b3be3f9f0c103f304c(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_GROUP_02a5a26c964e53b3be3f9f0c103f304c_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_group_update_ip_to_sgt_mapping_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_GROUP_73ebc15160cf5c0184d3eaff3be14508(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_GROUP_73ebc15160cf5c0184d3eaff3be14508_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_group_delete_ip_to_sgt_mapping_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_GROUP_680a1544a7125003b7803c0ed383f4bf(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_GROUP_680a1544a7125003b7803c0ed383f4bf_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_group_get_all_ip_to_sgt_mapping_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_GROUP_55c2e3af6da356009f6499f00a4115e9(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_GROUP_55c2e3af6da356009f6499f00a4115e9_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_group_create_ip_to_sgt_mapping_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_GROUP_14c9a2546739540eb2c1cb7c411836cb(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_GROUP_14c9a2546739540eb2c1cb7c411836cb_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_group_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_GROUP_a39fa17ffcd45736aa221dd27916e843(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_GROUP_a39fa17ffcd45736aa221dd27916e843_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_group_bulk_request_for_ip_to_sgt_mapping_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_GROUP_bb5f9095ca7953d3bdb16155e263f25a(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_GROUP_bb5f9095ca7953d3bdb16155e263f25a_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_group_monitor_bulk_status_ip_to_sgt_mapping_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'BulkStatus': {'bulkId': 'string', 'mediaType': 'string', 'executionStatus': 'string', 'operationType': 'string', 'startTime': 'string', 'resourcesCount': 0, 'successCount': 0, 'failCount': 0, 'resourcesStatus': [{'id': 'string', 'name': 'string', 'description': 'string', 'resourceExecutionStatus': 'string', 'status': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_b5711af534e557749661afb5b6c90cee(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_b5711af534e557749661afb5b6c90cee_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_deploy_ip_to_sgt_mapping_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_83343989df7a50feb38d8729b99553e9(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_83343989df7a50feb38d8729b99553e9_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_deploy_all_ip_to_sgt_mapping_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_dcd55e1e57d25e65b625526a1d341afd(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_dcd55e1e57d25e65b625526a1d341afd_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_get_deploy_status_ip_to_sgt_mapping_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'OperationResult': {'resultValue': [{'value': 'string', 'name': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_17ddc6729af25f8b8c060b20d09f0057(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_17ddc6729af25f8b8c060b20d09f0057_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_get_ip_to_sgt_mapping_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SGMapping': {'id': 'string', 'name': 'string', 'sgt': 'string', 'deployTo': 'string', 'deployType': 'string', 'hostName': 'string', 'hostIp': 'string', 'mappingGroup': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_94de3cecd62e5153881245a8613fbeea(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_94de3cecd62e5153881245a8613fbeea_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_update_ip_to_sgt_mapping_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_582650f0cb1e55c9baee89c136c8ec47(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_582650f0cb1e55c9baee89c136c8ec47_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_delete_ip_to_sgt_mapping_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_10cd9e91565f5c74b9f32ff0e5be6f17(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_10cd9e91565f5c74b9f32ff0e5be6f17_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_get_all_ip_to_sgt_mapping_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_52dd838b268f5dd298a123ac58448ea9(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_52dd838b268f5dd298a123ac58448ea9_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_create_ip_to_sgt_mapping_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_63042762af0b5041b56b12c5c08cc53e(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_63042762af0b5041b56b12c5c08cc53e_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_ab203a1dd0015924bf2005a84ae85477(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_ab203a1dd0015924bf2005a84ae85477_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_bulk_request_for_ip_to_sgt_mapping_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_IP_TO_SGT_MAPPING_9f36d3f43a6157978ec529318ce506e0(self):
        return re.search(
            self.IP_TO_SGT_MAPPING_9f36d3f43a6157978ec529318ce506e0_PATTERN,
            self.path
        )

    def ip_to_sgt_mapping_monitor_bulk_status_ip_to_sgt_mapping_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'BulkStatus': {'bulkId': 'string', 'mediaType': 'string', 'executionStatus': 'string', 'operationType': 'string', 'startTime': 'string', 'resourcesCount': 0, 'successCount': 0, 'failCount': 0, 'resourcesStatus': [{'id': 'string', 'name': 'string', 'description': 'string', 'resourceExecutionStatus': 'string', 'status': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MY_DEVICE_PORTAL_4bb3528d280652678f8e211b9e418e66(self):
        return re.search(
            self.MY_DEVICE_PORTAL_4bb3528d280652678f8e211b9e418e66_PATTERN,
            self.path
        )

    def my_device_portal_get_my_device_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'MyDevicePortal': {'id': 'string', 'name': 'string', 'description': 'string', 'portalType': 'string', 'portalTestUrl': 'string', 'settings': {'portalSettings': {'httpsPort': 0, 'allowedInterfaces': 'string', 'certificateGroupTag': 'string', 'endpointIdentityGroup': 'string', 'displayLang': 'string', 'fallbackLanguage': 'string', 'alwaysUsedLanguage': 'string'}, 'loginPageSettings': {'maxFailedAttemptsBeforeRateLimit': 0, 'timeBetweenLoginsDuringRateLimit': 0, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'requireScrolling': True, 'socialConfigs': [{}]}, 'aupSettings': {'displayFrequencyIntervalDays': 0, 'displayFrequency': 'string', 'includeAup': True, 'requireScrolling': True}, 'employeeChangePasswordSettings': {'allowEmployeeToChangePwd': True}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'postAccessBannerSettings': {'includePostAccessBanner': True}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string', 'defaultEmptyFieldValue': 'string'}}, 'customizations': {'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'backgroundImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MY_DEVICE_PORTAL_83079c64b769537ea7c586565f6ed2a2(self):
        return re.search(
            self.MY_DEVICE_PORTAL_83079c64b769537ea7c586565f6ed2a2_PATTERN,
            self.path
        )

    def my_device_portal_update_my_device_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MY_DEVICE_PORTAL_c04f18d6afee5f649a5700bf3074adb9(self):
        return re.search(
            self.MY_DEVICE_PORTAL_c04f18d6afee5f649a5700bf3074adb9_PATTERN,
            self.path
        )

    def my_device_portal_delete_my_device_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MY_DEVICE_PORTAL_90a71ccf29f05ee29af909b07bb9c754(self):
        return re.search(
            self.MY_DEVICE_PORTAL_90a71ccf29f05ee29af909b07bb9c754_PATTERN,
            self.path
        )

    def my_device_portal_get_all_my_device_portal_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MY_DEVICE_PORTAL_e643a5ac8bca55f58ea8d6260c57eafe(self):
        return re.search(
            self.MY_DEVICE_PORTAL_e643a5ac8bca55f58ea8d6260c57eafe_PATTERN,
            self.path
        )

    def my_device_portal_create_my_device_portal_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MY_DEVICE_PORTAL_5e356376df735e72aa55332951806f42(self):
        return re.search(
            self.MY_DEVICE_PORTAL_5e356376df735e72aa55332951806f42_PATTERN,
            self.path
        )

    def my_device_portal_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NATIVE_SUPPLICANT_PROFILE_5d1b9755414c5dcbb61987b2dd06839a(self):
        return re.search(
            self.NATIVE_SUPPLICANT_PROFILE_5d1b9755414c5dcbb61987b2dd06839a_PATTERN,
            self.path
        )

    def native_supplicant_profile_get_native_supplicant_profile_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSNSPProfile': {'id': 'string', 'name': 'string', 'description': 'string', 'wirelessProfiles': [{'ssid': 'string', 'allowedProtocol': 'string', 'certificateTemplateId': 'string', 'actionType': 'string', 'previousSsid': 'string'}], 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NATIVE_SUPPLICANT_PROFILE_c54a2ad63f46527dbec140a05f1213b7(self):
        return re.search(
            self.NATIVE_SUPPLICANT_PROFILE_c54a2ad63f46527dbec140a05f1213b7_PATTERN,
            self.path
        )

    def native_supplicant_profile_update_native_supplicant_profile_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NATIVE_SUPPLICANT_PROFILE_3fff9d421c78597d98a54dd08a9a99f9(self):
        return re.search(
            self.NATIVE_SUPPLICANT_PROFILE_3fff9d421c78597d98a54dd08a9a99f9_PATTERN,
            self.path
        )

    def native_supplicant_profile_delete_native_supplicant_profile_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NATIVE_SUPPLICANT_PROFILE_6470fa9802505d7bbdf85b951581db47(self):
        return re.search(
            self.NATIVE_SUPPLICANT_PROFILE_6470fa9802505d7bbdf85b951581db47_PATTERN,
            self.path
        )

    def native_supplicant_profile_get_all_native_supplicant_profile_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NATIVE_SUPPLICANT_PROFILE_f577c55d36b05178b0275dd88c71e118(self):
        return re.search(
            self.NATIVE_SUPPLICANT_PROFILE_f577c55d36b05178b0275dd88c71e118_PATTERN,
            self.path
        )

    def native_supplicant_profile_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_GROUP_e1d938f110e059a5abcb9cc8fb3cbd7c(self):
        return re.search(
            self.NETWORK_DEVICE_GROUP_e1d938f110e059a5abcb9cc8fb3cbd7c_PATTERN,
            self.path
        )

    def network_device_group_get_network_device_group_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'NetworkDeviceGroup': {'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}, 'othername': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_GROUP_a0fdb67d95475cd39382171dec96d6c1(self):
        return re.search(
            self.NETWORK_DEVICE_GROUP_a0fdb67d95475cd39382171dec96d6c1_PATTERN,
            self.path
        )

    def network_device_group_get_network_device_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'NetworkDeviceGroup': {'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}, 'othername': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_GROUP_808461e6734850fabb2097fa969948cb(self):
        return re.search(
            self.NETWORK_DEVICE_GROUP_808461e6734850fabb2097fa969948cb_PATTERN,
            self.path
        )

    def network_device_group_update_network_device_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_GROUP_9291975ded6653128f502c97e52cf279(self):
        return re.search(
            self.NETWORK_DEVICE_GROUP_9291975ded6653128f502c97e52cf279_PATTERN,
            self.path
        )

    def network_device_group_delete_network_device_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_GROUP_2a1af553d663556ca429a10ed82effda(self):
        return re.search(
            self.NETWORK_DEVICE_GROUP_2a1af553d663556ca429a10ed82effda_PATTERN,
            self.path
        )

    def network_device_group_get_all_network_device_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_GROUP_6c38fb2e2dd45f4dab6ec3a19effd15a(self):
        return re.search(
            self.NETWORK_DEVICE_GROUP_6c38fb2e2dd45f4dab6ec3a19effd15a_PATTERN,
            self.path
        )

    def network_device_group_create_network_device_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_GROUP_163f22d64bd4557d856a66ad6599d2d1(self):
        return re.search(
            self.NETWORK_DEVICE_GROUP_163f22d64bd4557d856a66ad6599d2d1_PATTERN,
            self.path
        )

    def network_device_group_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_54d8610d4a355b63aaaa364447d5fa00(self):
        return re.search(
            self.NETWORK_DEVICE_54d8610d4a355b63aaaa364447d5fa00_PATTERN,
            self.path
        )

    def network_device_get_network_device_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'NetworkDevice': {'id': 'string', 'name': 'string', 'description': 'string', 'authenticationSettings': {'networkProtocol': 'string', 'secondRadiusSharedSecret': 'string', 'radiusSharedSecret': 'string', 'enableKeyWrap': True, 'enabled': True, 'dtlsRequired': True, 'enableMultiSecret': True, 'keyEncryptionKey': 'string', 'messageAuthenticatorCodeKey': 'string', 'keyInputFormat': 'string'}, 'snmpsettings': {'version': 'string', 'roCommunity': 'string', 'pollingInterval': 0, 'linkTrapQuery': True, 'macTrapQuery': True, 'originatingPolicyServicesNode': 'string'}, 'trustsecsettings': {'deviceAuthenticationSettings': {'sgaDeviceId': 'string', 'sgaDevicePassword': 'string'}, 'sgaNotificationAndUpdates': {'downlaodEnvironmentDataEveryXSeconds': 0, 'downlaodPeerAuthorizationPolicyEveryXSeconds': 0, 'reAuthenticationEveryXSeconds': 0, 'downloadSGACLListsEveryXSeconds': 0, 'otherSGADevicesToTrustThisDevice': True, 'sendConfigurationToDevice': True, 'sendConfigurationToDeviceUsing': 'string', 'coaSourceHost': 'string'}, 'deviceConfigurationDeployment': {'includeWhenDeployingSGTUpdates': True, 'enableModePassword': 'string', 'execModePassword': 'string', 'execModeUsername': 'string'}, 'pushIdSupport': True}, 'tacacsSettings': {'sharedSecret': 'string', 'connectModeOptions': 'string'}, 'profileName': 'string', 'modelName': 'string', 'softwareVersion': 'string', 'coaPort': 0, 'dtlsDnsName': 'string', 'NetworkDeviceIPList': [{'ipaddress': 'string', 'mask': 0, 'getIpaddressExclude': 'string'}], 'NetworkDeviceGroupList': ['string'], 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_2ea2c4586b845888b2a9375126f70de2(self):
        return re.search(
            self.NETWORK_DEVICE_2ea2c4586b845888b2a9375126f70de2_PATTERN,
            self.path
        )

    def network_device_update_network_device_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_116eafaf2e785c6898fb982dbe4462e7(self):
        return re.search(
            self.NETWORK_DEVICE_116eafaf2e785c6898fb982dbe4462e7_PATTERN,
            self.path
        )

    def network_device_delete_network_device_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_a4ab683ce53052e089626a096abaf451(self):
        return re.search(
            self.NETWORK_DEVICE_a4ab683ce53052e089626a096abaf451_PATTERN,
            self.path
        )

    def network_device_get_network_device_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'NetworkDevice': {'id': 'string', 'name': 'string', 'description': 'string', 'authenticationSettings': {'networkProtocol': 'string', 'secondRadiusSharedSecret': 'string', 'radiusSharedSecret': 'string', 'enableKeyWrap': True, 'enabled': True, 'dtlsRequired': True, 'enableMultiSecret': True, 'keyEncryptionKey': 'string', 'messageAuthenticatorCodeKey': 'string', 'keyInputFormat': 'string'}, 'snmpsettings': {'version': 'string', 'roCommunity': 'string', 'pollingInterval': 0, 'linkTrapQuery': True, 'macTrapQuery': True, 'originatingPolicyServicesNode': 'string'}, 'trustsecsettings': {'deviceAuthenticationSettings': {'sgaDeviceId': 'string', 'sgaDevicePassword': 'string'}, 'sgaNotificationAndUpdates': {'downlaodEnvironmentDataEveryXSeconds': 0, 'downlaodPeerAuthorizationPolicyEveryXSeconds': 0, 'reAuthenticationEveryXSeconds': 0, 'downloadSGACLListsEveryXSeconds': 0, 'otherSGADevicesToTrustThisDevice': True, 'sendConfigurationToDevice': True, 'sendConfigurationToDeviceUsing': 'string', 'coaSourceHost': 'string'}, 'deviceConfigurationDeployment': {'includeWhenDeployingSGTUpdates': True, 'enableModePassword': 'string', 'execModePassword': 'string', 'execModeUsername': 'string'}, 'pushIdSupport': True}, 'tacacsSettings': {'sharedSecret': 'string', 'connectModeOptions': 'string'}, 'profileName': 'string', 'coaPort': 0, 'dtlsDnsName': 'string', 'modelName': 'string', 'softwareVersion': 'string', 'NetworkDeviceIPList': [{'ipaddress': 'string', 'mask': 0, 'getIpaddressExclude': 'string'}], 'NetworkDeviceGroupList': ['string'], 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_b1edfeb182025176bb250633937177ae(self):
        return re.search(
            self.NETWORK_DEVICE_b1edfeb182025176bb250633937177ae_PATTERN,
            self.path
        )

    def network_device_update_network_device_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_9f2fd3c6324b581ca0f3f9eadede1cdc(self):
        return re.search(
            self.NETWORK_DEVICE_9f2fd3c6324b581ca0f3f9eadede1cdc_PATTERN,
            self.path
        )

    def network_device_delete_network_device_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_48b986fa0f0d54ef98eb135eeb88808a(self):
        return re.search(
            self.NETWORK_DEVICE_48b986fa0f0d54ef98eb135eeb88808a_PATTERN,
            self.path
        )

    def network_device_get_all_network_device_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_574ca6ab8ec556c3bc9531dc380b230a(self):
        return re.search(
            self.NETWORK_DEVICE_574ca6ab8ec556c3bc9531dc380b230a_PATTERN,
            self.path
        )

    def network_device_create_network_device_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_682601e571185718b6ef6e78bfbfdf68(self):
        return re.search(
            self.NETWORK_DEVICE_682601e571185718b6ef6e78bfbfdf68_PATTERN,
            self.path
        )

    def network_device_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_63b2eebd5c245e58a503aa53115eec53(self):
        return re.search(
            self.NETWORK_DEVICE_63b2eebd5c245e58a503aa53115eec53_PATTERN,
            self.path
        )

    def network_device_bulk_request_for_network_device_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_NETWORK_DEVICE_1bf96800cc265b5e9e1566ec7088619c(self):
        return re.search(
            self.NETWORK_DEVICE_1bf96800cc265b5e9e1566ec7088619c_PATTERN,
            self.path
        )

    def network_device_monitor_bulk_status_network_device_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'BulkStatus': {'bulkId': 'string', 'mediaType': 'string', 'executionStatus': 'string', 'operationType': 'string', 'startTime': 'string', 'resourcesCount': 0, 'successCount': 0, 'failCount': 0, 'resourcesStatus': [{'id': 'string', 'name': 'string', 'description': 'string', 'resourceExecutionStatus': 'string', 'status': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PORTAL_GLOBAL_SETTING_0ac243ecb8c157658a4bcfe77a102c14(self):
        return re.search(
            self.PORTAL_GLOBAL_SETTING_0ac243ecb8c157658a4bcfe77a102c14_PATTERN,
            self.path
        )

    def portal_global_setting_get_portal_global_setting_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'PortalCustomizationGlobalSetting': {'id': 'string', 'customization': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PORTAL_GLOBAL_SETTING_c97e7851003e5a63a2a8005ac8807dc7(self):
        return re.search(
            self.PORTAL_GLOBAL_SETTING_c97e7851003e5a63a2a8005ac8807dc7_PATTERN,
            self.path
        )

    def portal_global_setting_update_portal_global_setting_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PORTAL_GLOBAL_SETTING_e9ce4a1e1cf955f098343646760e9d58(self):
        return re.search(
            self.PORTAL_GLOBAL_SETTING_e9ce4a1e1cf955f098343646760e9d58_PATTERN,
            self.path
        )

    def portal_global_setting_get_all_portal_global_settings_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PORTAL_GLOBAL_SETTING_a9a99c0aacce5a8181e2ff79bf99ae20(self):
        return re.search(
            self.PORTAL_GLOBAL_SETTING_a9a99c0aacce5a8181e2ff79bf99ae20_PATTERN,
            self.path
        )

    def portal_global_setting_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PORTAL_THEME_6e58eabefef15feb880ecfe2906d805f(self):
        return re.search(
            self.PORTAL_THEME_6e58eabefef15feb880ecfe2906d805f_PATTERN,
            self.path
        )

    def portal_theme_get_portal_theme_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'PortalTheme': {'id': 'string', 'name': 'string', 'description': 'string', 'themeData': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PORTAL_THEME_c82dcf6f2c3d5d399045050b02208db2(self):
        return re.search(
            self.PORTAL_THEME_c82dcf6f2c3d5d399045050b02208db2_PATTERN,
            self.path
        )

    def portal_theme_update_portal_theme_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PORTAL_THEME_8567c39e537955888cc23e4f90e6449b(self):
        return re.search(
            self.PORTAL_THEME_8567c39e537955888cc23e4f90e6449b_PATTERN,
            self.path
        )

    def portal_theme_delete_portal_theme_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PORTAL_THEME_5ad233598ed75e0c97ddd3c3f1af50e4(self):
        return re.search(
            self.PORTAL_THEME_5ad233598ed75e0c97ddd3c3f1af50e4_PATTERN,
            self.path
        )

    def portal_theme_get_all_portal_themes_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PORTAL_THEME_91eb833980f55025bfacbfcb8de814c8(self):
        return re.search(
            self.PORTAL_THEME_91eb833980f55025bfacbfcb8de814c8_PATTERN,
            self.path
        )

    def portal_theme_create_portal_theme_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PORTAL_THEME_b6bf4f02759a5e7f968896a30575e4c6(self):
        return re.search(
            self.PORTAL_THEME_b6bf4f02759a5e7f968896a30575e4c6_PATTERN,
            self.path
        )

    def portal_theme_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PORTAL_5ce70db7732c596aa82bd7d1725ac02d(self):
        return re.search(
            self.PORTAL_5ce70db7732c596aa82bd7d1725ac02d_PATTERN,
            self.path
        )

    def portal_get_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSPortal': {'id': 'string', 'name': 'string', 'description': 'string', 'portalType': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PORTAL_2a72ae8af1075d0c94912b008003b13e(self):
        return re.search(
            self.PORTAL_2a72ae8af1075d0c94912b008003b13e_PATTERN,
            self.path
        )

    def portal_get_all_portals_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PORTAL_1d754ad0697d54c98c2690c5043e0be6(self):
        return re.search(
            self.PORTAL_1d754ad0697d54c98c2690c5043e0be6_PATTERN,
            self.path
        )

    def portal_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PROFILER_PROFILE_0e176356698b5ec49609504a530c1d8a(self):
        return re.search(
            self.PROFILER_PROFILE_0e176356698b5ec49609504a530c1d8a_PATTERN,
            self.path
        )

    def profiler_profile_get_profiler_profile_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ProfilerProfile': {'id': 'string', 'name': 'string', 'description': 'string', 'parentId': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PROFILER_PROFILE_688d53f6d85a5d609d49bd38cfd65e57(self):
        return re.search(
            self.PROFILER_PROFILE_688d53f6d85a5d609d49bd38cfd65e57_PATTERN,
            self.path
        )

    def profiler_profile_get_all_profiler_profiles_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PROFILER_PROFILE_de35c041dc1456cca42b7b2e32a4713d(self):
        return re.search(
            self.PROFILER_PROFILE_de35c041dc1456cca42b7b2e32a4713d_PATTERN,
            self.path
        )

    def profiler_profile_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PX_GRID_SETTINGS_787126e5dd9b5979a409b9f456265db0(self):
        return re.search(
            self.PX_GRID_SETTINGS_787126e5dd9b5979a409b9f456265db0_PATTERN,
            self.path
        )

    def px_grid_settings_autoapprove_px_grid_settings_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PX_GRID_SETTINGS_bea00c7a4f9b5e1798ea078e123ff016(self):
        return re.search(
            self.PX_GRID_SETTINGS_bea00c7a4f9b5e1798ea078e123ff016_PATTERN,
            self.path
        )

    def px_grid_settings_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_RADIUS_SERVER_SEQUENCE_0d1df0e230765104863b8d63d5beb68e(self):
        return re.search(
            self.RADIUS_SERVER_SEQUENCE_0d1df0e230765104863b8d63d5beb68e_PATTERN,
            self.path
        )

    def radius_server_sequence_get_radius_server_sequence_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'RadiusServerSequence': {'id': 'string', 'name': 'string', 'description': 'string', 'stripPrefix': True, 'stripSuffix': True, 'prefixSeparator': 'string', 'suffixSeparator': 'string', 'remoteAccounting': True, 'localAccounting': True, 'useAttrSetOnRequest': True, 'useAttrSetBeforeAcc': True, 'continueAuthorzPolicy': True, 'RadiusServerList': ['string'], 'OnRequestAttrManipulatorList': [{'action': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'value': 'string', 'changedVal': 'string'}], 'BeforeAcceptAttrManipulatorsList': [{'action': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'value': 'string', 'changedVal': 'string'}], 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_RADIUS_SERVER_SEQUENCE_df9ab8ff636353279d5c787585dcb6af(self):
        return re.search(
            self.RADIUS_SERVER_SEQUENCE_df9ab8ff636353279d5c787585dcb6af_PATTERN,
            self.path
        )

    def radius_server_sequence_update_radius_server_sequence_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_RADIUS_SERVER_SEQUENCE_815b13838fa75d6e8d970f6eeb6a4510(self):
        return re.search(
            self.RADIUS_SERVER_SEQUENCE_815b13838fa75d6e8d970f6eeb6a4510_PATTERN,
            self.path
        )

    def radius_server_sequence_delete_radius_server_sequence_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_RADIUS_SERVER_SEQUENCE_c6c330dace185a548f70f4e5d67776ea(self):
        return re.search(
            self.RADIUS_SERVER_SEQUENCE_c6c330dace185a548f70f4e5d67776ea_PATTERN,
            self.path
        )

    def radius_server_sequence_get_all_radius_server_sequence_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_RADIUS_SERVER_SEQUENCE_83ad6ca0642c5750af6ca9905721a9d7(self):
        return re.search(
            self.RADIUS_SERVER_SEQUENCE_83ad6ca0642c5750af6ca9905721a9d7_PATTERN,
            self.path
        )

    def radius_server_sequence_create_radius_server_sequence_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_RADIUS_SERVER_SEQUENCE_8fb1a72ded19590fa0aa85fc59ea8cfc(self):
        return re.search(
            self.RADIUS_SERVER_SEQUENCE_8fb1a72ded19590fa0aa85fc59ea8cfc_PATTERN,
            self.path
        )

    def radius_server_sequence_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_RESTID_STORE_17a5f22fc961547f93976a53949cac73(self):
        return re.search(
            self.RESTID_STORE_17a5f22fc961547f93976a53949cac73_PATTERN,
            self.path
        )

    def restid_store_get_rest_id_store_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSRestIDStore': {'id': 'string', 'name': 'string', 'description': 'string', 'ersRestIDStoreAttributes': {'usernameSuffix': 'string', 'rootUrl': 'string', 'predefined': 'string', 'headers': [{'key': 'string', 'value': 'string'}]}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_RESTID_STORE_c85464a04f0e5ddc99f8e6b8ed0f7eac(self):
        return re.search(
            self.RESTID_STORE_c85464a04f0e5ddc99f8e6b8ed0f7eac_PATTERN,
            self.path
        )

    def restid_store_update_rest_id_store_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_RESTID_STORE_e068a8dc1ed65f8d9cdfa70a49f543e0(self):
        return re.search(
            self.RESTID_STORE_e068a8dc1ed65f8d9cdfa70a49f543e0_PATTERN,
            self.path
        )

    def restid_store_delete_rest_id_store_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_RESTID_STORE_788cba3f7ace597da668acfbe00364be(self):
        return re.search(
            self.RESTID_STORE_788cba3f7ace597da668acfbe00364be_PATTERN,
            self.path
        )

    def restid_store_get_rest_id_store_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSRestIDStore': {'name': 'string', 'description': 'string', 'ersRestIDStoreAttributes': {'usernameSuffix': 'string', 'rootUrl': 'string', 'predefined': 'string', 'headers': [{'key': 'string', 'value': 'string'}]}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_RESTID_STORE_ded7f8573c255c318bb1f04bfdbf01e1(self):
        return re.search(
            self.RESTID_STORE_ded7f8573c255c318bb1f04bfdbf01e1_PATTERN,
            self.path
        )

    def restid_store_update_rest_id_store_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_RESTID_STORE_2e77a1dd4aa75dcebbc3ee4e94a162b4(self):
        return re.search(
            self.RESTID_STORE_2e77a1dd4aa75dcebbc3ee4e94a162b4_PATTERN,
            self.path
        )

    def restid_store_delete_rest_id_store_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_RESTID_STORE_d810359e31e453ac8145981b7d5bb7e4(self):
        return re.search(
            self.RESTID_STORE_d810359e31e453ac8145981b7d5bb7e4_PATTERN,
            self.path
        )

    def restid_store_get_all_rest_id_store_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_RESTID_STORE_1073c23243c950f29b51f502c03d7058(self):
        return re.search(
            self.RESTID_STORE_1073c23243c950f29b51f502c03d7058_PATTERN,
            self.path
        )

    def restid_store_create_rest_id_store_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_RESTID_STORE_1b8c3846fcf751e4b008eb0a011dea4d(self):
        return re.search(
            self.RESTID_STORE_1b8c3846fcf751e4b008eb0a011dea4d_PATTERN,
            self.path
        )

    def restid_store_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUPS_ACLS_a50d1bd34d5f593aadf8eb02083c67b0(self):
        return re.search(
            self.SECURITY_GROUPS_ACLS_a50d1bd34d5f593aadf8eb02083c67b0_PATTERN,
            self.path
        )

    def security_groups_acls_get_security_groups_acl_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'Sgacl': {'id': 'string', 'name': 'string', 'description': 'string', 'generationId': 'string', 'aclcontent': 'string', 'isReadOnly': True, 'modelledContent': {}, 'ipVersion': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUPS_ACLS_afc81cd1e25c50319f75606b97c23b3d(self):
        return re.search(
            self.SECURITY_GROUPS_ACLS_afc81cd1e25c50319f75606b97c23b3d_PATTERN,
            self.path
        )

    def security_groups_acls_update_security_groups_acl_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUPS_ACLS_b0a2bea8bfec52b68663ef3f7ac6d7a7(self):
        return re.search(
            self.SECURITY_GROUPS_ACLS_b0a2bea8bfec52b68663ef3f7ac6d7a7_PATTERN,
            self.path
        )

    def security_groups_acls_delete_security_groups_acl_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUPS_ACLS_999b22d6ad9f595ab7e3eee5cf44de8a(self):
        return re.search(
            self.SECURITY_GROUPS_ACLS_999b22d6ad9f595ab7e3eee5cf44de8a_PATTERN,
            self.path
        )

    def security_groups_acls_get_all_security_groups_acl_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUPS_ACLS_9ab61f24bdaf508590f7686e1130913f(self):
        return re.search(
            self.SECURITY_GROUPS_ACLS_9ab61f24bdaf508590f7686e1130913f_PATTERN,
            self.path
        )

    def security_groups_acls_create_security_groups_acl_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUPS_ACLS_6704e67a1131578aa794d8377da9a1de(self):
        return re.search(
            self.SECURITY_GROUPS_ACLS_6704e67a1131578aa794d8377da9a1de_PATTERN,
            self.path
        )

    def security_groups_acls_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUPS_ACLS_bfff136597e25df5ae1d135251fee263(self):
        return re.search(
            self.SECURITY_GROUPS_ACLS_bfff136597e25df5ae1d135251fee263_PATTERN,
            self.path
        )

    def security_groups_acls_bulk_request_for_security_groups_acl_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUPS_ACLS_07af5ee576605a5a915d888924c1e804(self):
        return re.search(
            self.SECURITY_GROUPS_ACLS_07af5ee576605a5a915d888924c1e804_PATTERN,
            self.path
        )

    def security_groups_acls_monitor_bulk_status_security_groups_acl_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'BulkStatus': {'bulkId': 'string', 'mediaType': 'string', 'executionStatus': 'string', 'operationType': 'string', 'startTime': 'string', 'resourcesCount': 0, 'successCount': 0, 'failCount': 0, 'resourcesStatus': [{'id': 'string', 'name': 'string', 'description': 'string', 'resourceExecutionStatus': 'string', 'status': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUP_TO_VIRTUAL_NETWORK_2112393ea0a65da3ae0346b912a9efac(self):
        return re.search(
            self.SECURITY_GROUP_TO_VIRTUAL_NETWORK_2112393ea0a65da3ae0346b912a9efac_PATTERN,
            self.path
        )

    def security_group_to_virtual_network_get_security_groups_to_vn_to_vlan_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SgtVNVlanContainer': {'id': 'string', 'name': 'string', 'description': 'string', 'sgtId': 'string', 'virtualnetworklist': [{'id': 'string', 'name': 'string', 'description': 'string', 'defaultVirtualNetwork': True, 'vlans': [{'id': 'string', 'name': 'string', 'description': 'string', 'defaultVlan': True, 'maxValue': 0, 'data': True}]}], 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUP_TO_VIRTUAL_NETWORK_eae98db0c24b5ecca77cce8279e20785(self):
        return re.search(
            self.SECURITY_GROUP_TO_VIRTUAL_NETWORK_eae98db0c24b5ecca77cce8279e20785_PATTERN,
            self.path
        )

    def security_group_to_virtual_network_update_security_groups_to_vn_to_vlan_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUP_TO_VIRTUAL_NETWORK_9462680497c852dbb953860bef3326e0(self):
        return re.search(
            self.SECURITY_GROUP_TO_VIRTUAL_NETWORK_9462680497c852dbb953860bef3326e0_PATTERN,
            self.path
        )

    def security_group_to_virtual_network_delete_security_groups_to_vn_to_vlan_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUP_TO_VIRTUAL_NETWORK_e51b6e745cdb5bdda4de26a27b8d92bb(self):
        return re.search(
            self.SECURITY_GROUP_TO_VIRTUAL_NETWORK_e51b6e745cdb5bdda4de26a27b8d92bb_PATTERN,
            self.path
        )

    def security_group_to_virtual_network_get_all_security_groups_to_vn_to_vlan_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUP_TO_VIRTUAL_NETWORK_97830a0710ba581da4d3fd00e84d59e3(self):
        return re.search(
            self.SECURITY_GROUP_TO_VIRTUAL_NETWORK_97830a0710ba581da4d3fd00e84d59e3_PATTERN,
            self.path
        )

    def security_group_to_virtual_network_create_security_groups_to_vn_to_vlan_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUP_TO_VIRTUAL_NETWORK_7b2811387f4e55c8839c94ea241a3236(self):
        return re.search(
            self.SECURITY_GROUP_TO_VIRTUAL_NETWORK_7b2811387f4e55c8839c94ea241a3236_PATTERN,
            self.path
        )

    def security_group_to_virtual_network_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUP_TO_VIRTUAL_NETWORK_0ff196187ee45a92bf195593ab8f102e(self):
        return re.search(
            self.SECURITY_GROUP_TO_VIRTUAL_NETWORK_0ff196187ee45a92bf195593ab8f102e_PATTERN,
            self.path
        )

    def security_group_to_virtual_network_bulk_request_for_security_groups_to_vn_to_vlan_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUP_TO_VIRTUAL_NETWORK_10ea793a0b1b5ac498f7bc74a0aba257(self):
        return re.search(
            self.SECURITY_GROUP_TO_VIRTUAL_NETWORK_10ea793a0b1b5ac498f7bc74a0aba257_PATTERN,
            self.path
        )

    def security_group_to_virtual_network_monitor_bulk_status_security_groups_to_vn_to_vlan_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'BulkStatus': {'bulkId': 'string', 'mediaType': 'string', 'executionStatus': 'string', 'operationType': 'string', 'startTime': 'string', 'resourcesCount': 0, 'successCount': 0, 'failCount': 0, 'resourcesStatus': [{'id': 'string', 'name': 'string', 'description': 'string', 'resourceExecutionStatus': 'string', 'status': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUPS_ea658190e73c5ce1b27e7def4aea28e3(self):
        return re.search(
            self.SECURITY_GROUPS_ea658190e73c5ce1b27e7def4aea28e3_PATTERN,
            self.path
        )

    def security_groups_get_security_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'Sgt': {'id': 'string', 'name': 'string', 'description': 'string', 'value': 0, 'generationId': 0, 'isReadOnly': True, 'propogateToApic': True, 'defaultSGACLs': [{}], 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUPS_42ce666e64a958229cfd8da70945935e(self):
        return re.search(
            self.SECURITY_GROUPS_42ce666e64a958229cfd8da70945935e_PATTERN,
            self.path
        )

    def security_groups_update_security_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUPS_ed2c0f81f4ea5299840089761bfd4f62(self):
        return re.search(
            self.SECURITY_GROUPS_ed2c0f81f4ea5299840089761bfd4f62_PATTERN,
            self.path
        )

    def security_groups_delete_security_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUPS_b3c356cfc48a5da4b13b8ecbae5748b7(self):
        return re.search(
            self.SECURITY_GROUPS_b3c356cfc48a5da4b13b8ecbae5748b7_PATTERN,
            self.path
        )

    def security_groups_get_all_security_groups_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUPS_1d0290eb241f5bd79221afc8d6cb32da(self):
        return re.search(
            self.SECURITY_GROUPS_1d0290eb241f5bd79221afc8d6cb32da_PATTERN,
            self.path
        )

    def security_groups_create_security_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUPS_ad87f41ef4845f19a19bfadac0928ae6(self):
        return re.search(
            self.SECURITY_GROUPS_ad87f41ef4845f19a19bfadac0928ae6_PATTERN,
            self.path
        )

    def security_groups_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUPS_fe0ac7fc07885c6f877768654aefd189(self):
        return re.search(
            self.SECURITY_GROUPS_fe0ac7fc07885c6f877768654aefd189_PATTERN,
            self.path
        )

    def security_groups_bulk_request_for_security_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SECURITY_GROUPS_a3148b789a935070b99caed1e99592cf(self):
        return re.search(
            self.SECURITY_GROUPS_a3148b789a935070b99caed1e99592cf_PATTERN,
            self.path
        )

    def security_groups_monitor_bulk_status_security_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'BulkStatus': {'bulkId': 'string', 'mediaType': 'string', 'executionStatus': 'string', 'operationType': 'string', 'startTime': 'string', 'resourcesCount': 0, 'successCount': 0, 'failCount': 0, 'resourcesStatus': [{'id': 'string', 'name': 'string', 'description': 'string', 'resourceExecutionStatus': 'string', 'status': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SELF_REGISTERED_PORTAL_f9c9a5e917af53dbbb91733e82e72ebe(self):
        return re.search(
            self.SELF_REGISTERED_PORTAL_f9c9a5e917af53dbbb91733e82e72ebe_PATTERN,
            self.path
        )

    def self_registered_portal_get_self_registered_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SelfRegPortal': {'id': 'string', 'name': 'string', 'description': 'string', 'portalType': 'string', 'portalTestUrl': 'string', 'settings': {'portalSettings': {'httpsPort': 0, 'allowedInterfaces': 'string', 'certificateGroupTag': 'string', 'authenticationMethod': 'string', 'assignedGuestTypeForEmployee': 'string', 'displayLang': 'string', 'fallbackLanguage': 'string', 'alwaysUsedLanguage': 'string'}, 'loginPageSettings': {'requireAccessCode': True, 'maxFailedAttemptsBeforeRateLimit': 0, 'timeBetweenLoginsDuringRateLimit': 0, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'accessCode': 'string', 'allowGuestToCreateAccounts': True, 'allowForgotPassword': True, 'allowGuestToChangePassword': True, 'allowAlternateGuestPortal': True, 'alternateGuestPortal': 'string', 'allowGuestToUseSocialAccounts': True, 'allowShowGuestForm': True, 'socialConfigs': [{'socialMediaType': 'string', 'socialMediaValue': 'string'}]}, 'selfRegPageSettings': {'assignGuestsToGuestType': 'string', 'accountValidityDuration': 0, 'accountValidityTimeUnits': 'string', 'requireRegistrationCode': True, 'registrationCode': 'string', 'fieldUserName': {'include': True, 'require': True}, 'fieldFirstName': {'include': True, 'require': True}, 'fieldLastName': {'include': True, 'require': True}, 'fieldEmailAddr': {'include': True, 'require': True}, 'fieldPhoneNo': {'include': True, 'require': True}, 'fieldCompany': {'include': True, 'require': True}, 'fieldLocation': {'include': True, 'require': True}, 'selectableLocations': ['string'], 'fieldSmsProvider': {'include': True, 'require': True}, 'selectableSmsProviders': ['string'], 'fieldPersonBeingVisited': {'include': True, 'require': True}, 'fieldReasonForVisit': {'include': True, 'require': True}, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'enableGuestEmailWhitelist': True, 'guestEmailWhitelistDomains': 'string', 'enableGuestEmailBlacklist': True, 'guestEmailBlacklistDomains': 'string', 'requireGuestApproval': True, 'autoLoginSelfWait': True, 'autoLoginTimePeriod': 0, 'allowGraceAccess': True, 'graceAccessExpireInterval': 0, 'graceAccessSendAccountExpiration': True, 'sendApprovalRequestTo': 'string', 'approvalEmailAddresses': 'string', 'postRegistrationRedirect': 'string', 'postRegistrationRedirectUrl': 'string', 'credentialNotificationUsingEmail': True, 'credentialNotificationUsingSms': True, 'approveDenyLinksValidFor': 0, 'approveDenyLinksTimeUnits': 'string', 'requireApproverToAuthenticate': True, 'authenticateSponsorsUsingPortalList': 'string', 'sponsorPortalList': []}, 'selfRegSuccessSettings': {'includeUserName': True, 'includePassword': True, 'includeFirstName': True, 'includeLastName': True, 'includeEmailAddr': True, 'includePhoneNo': True, 'includeCompany': True, 'includeLocation': True, 'includeSmsProvider': True, 'includePersonBeingVisited': True, 'includeReasonForVisit': True, 'allowGuestSendSelfUsingPrint': True, 'allowGuestSendSelfUsingEmail': True, 'allowGuestSendSelfUsingSms': True, 'includeAup': True, 'aupOnPage': True, 'requireAupAcceptance': True, 'requireAupScrolling': True, 'allowGuestLoginFromSelfregSuccessPage': True}, 'aupSettings': {'includeAup': True, 'useDiffAupForEmployees': True, 'skipAupForEmployees': True, 'requireScrolling': True, 'requireAupScrolling': True, 'displayFrequency': 'string', 'displayFrequencyIntervalDays': 0}, 'guestChangePasswordSettings': {'allowChangePasswdAtFirstLogin': True}, 'guestDeviceRegistrationSettings': {'autoRegisterGuestDevices': True, 'allowGuestsToRegisterDevices': True}, 'byodSettings': {'byodWelcomeSettings': {'enableBYOD': True, 'enableGuestAccess': True, 'requireMDM': True, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'requireScrolling': True}, 'byodRegistrationSettings': {'showDeviceID': True, 'endPointIdentityGroupId': 'string'}, 'byodRegistrationSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'postAccessBannerSettings': {'includePostAccessBanner': True}, 'authSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string', 'defaultEmptyFieldValue': 'string'}}, 'customizations': {'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'backgroundImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SELF_REGISTERED_PORTAL_400c4fada6c558d9aba09cc373d5b266(self):
        return re.search(
            self.SELF_REGISTERED_PORTAL_400c4fada6c558d9aba09cc373d5b266_PATTERN,
            self.path
        )

    def self_registered_portal_update_self_registered_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SELF_REGISTERED_PORTAL_673f9ada2e275fa2934fdb4825266a2c(self):
        return re.search(
            self.SELF_REGISTERED_PORTAL_673f9ada2e275fa2934fdb4825266a2c_PATTERN,
            self.path
        )

    def self_registered_portal_delete_self_registered_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SELF_REGISTERED_PORTAL_bb165bd00a6653ac9da440f23ee62ecc(self):
        return re.search(
            self.SELF_REGISTERED_PORTAL_bb165bd00a6653ac9da440f23ee62ecc_PATTERN,
            self.path
        )

    def self_registered_portal_get_all_self_registered_portals_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SELF_REGISTERED_PORTAL_d524614e122d53d68324daf1681eb753(self):
        return re.search(
            self.SELF_REGISTERED_PORTAL_d524614e122d53d68324daf1681eb753_PATTERN,
            self.path
        )

    def self_registered_portal_create_self_registered_portal_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SELF_REGISTERED_PORTAL_3d8cc0e6962558c58d263f53b857cff0(self):
        return re.search(
            self.SELF_REGISTERED_PORTAL_3d8cc0e6962558c58d263f53b857cff0_PATTERN,
            self.path
        )

    def self_registered_portal_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SMS_PROVIDER_17daac88943a5cd2bd745c483448e231(self):
        return re.search(
            self.SMS_PROVIDER_17daac88943a5cd2bd745c483448e231_PATTERN,
            self.path
        )

    def sms_provider_get_all_sms_provider_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SMS_PROVIDER_37250017e20e5400a53280d52487ecd6(self):
        return re.search(
            self.SMS_PROVIDER_37250017e20e5400a53280d52487ecd6_PATTERN,
            self.path
        )

    def sms_provider_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSOR_GROUP_MEMBER_020659d6b1385f4cb9381c13a1fa4356(self):
        return re.search(
            self.SPONSOR_GROUP_MEMBER_020659d6b1385f4cb9381c13a1fa4356_PATTERN,
            self.path
        )

    def sponsor_group_member_get_all_sponsor_group_member_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSOR_GROUP_MEMBER_0f7c916a2e265c11b8b8535e8f88c7d1(self):
        return re.search(
            self.SPONSOR_GROUP_MEMBER_0f7c916a2e265c11b8b8535e8f88c7d1_PATTERN,
            self.path
        )

    def sponsor_group_member_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSOR_GROUP_eaa0d7c339d152b688876c2e10f51fe7(self):
        return re.search(
            self.SPONSOR_GROUP_eaa0d7c339d152b688876c2e10f51fe7_PATTERN,
            self.path
        )

    def sponsor_group_get_sponsor_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SponsorGroup': {'id': 'string', 'name': 'string', 'description': 'string', 'isEnabled': True, 'isDefaultGroup': True, 'memberGroups': ['string'], 'guestTypes': ['string'], 'locations': ['string'], 'autoNotification': True, 'createPermissions': {'canImportMultipleAccounts': True, 'importBatchSizeLimit': 0, 'canCreateRandomAccounts': True, 'randomBatchSizeLimit': 0, 'defaultUsernamePrefix': 'string', 'canSpecifyUsernamePrefix': True, 'canSetFutureStartDate': True, 'startDateFutureLimitDays': 0}, 'managePermission': 'string', 'otherPermissions': {'canUpdateGuestContactInfo': True, 'canViewGuestPasswords': True, 'canSendSmsNotifications': True, 'canResetGuestPasswords': True, 'canExtendGuestAccounts': True, 'canDeleteGuestAccounts': True, 'canSuspendGuestAccounts': True, 'requireSuspensionReason': True, 'canReinstateSuspendedAccounts': True, 'canApproveSelfregGuests': True, 'limitApprovalToSponsorsGuests': True, 'canAccessViaRest': True}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSOR_GROUP_dfc44f7f24d153d789efa48e904b3832(self):
        return re.search(
            self.SPONSOR_GROUP_dfc44f7f24d153d789efa48e904b3832_PATTERN,
            self.path
        )

    def sponsor_group_update_sponsor_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSOR_GROUP_61c28a45acf05fec98879d8d2ac51129(self):
        return re.search(
            self.SPONSOR_GROUP_61c28a45acf05fec98879d8d2ac51129_PATTERN,
            self.path
        )

    def sponsor_group_delete_sponsor_group_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSOR_GROUP_f1196f1f6fde5978b0522f096926d443(self):
        return re.search(
            self.SPONSOR_GROUP_f1196f1f6fde5978b0522f096926d443_PATTERN,
            self.path
        )

    def sponsor_group_get_all_sponsor_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSOR_GROUP_56311acd30d35ee2ae16ff23757de7d8(self):
        return re.search(
            self.SPONSOR_GROUP_56311acd30d35ee2ae16ff23757de7d8_PATTERN,
            self.path
        )

    def sponsor_group_create_sponsor_group_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSOR_GROUP_e8d4001b740751e08cfc19e1fdc5fddf(self):
        return re.search(
            self.SPONSOR_GROUP_e8d4001b740751e08cfc19e1fdc5fddf_PATTERN,
            self.path
        )

    def sponsor_group_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSOR_PORTAL_cd6793a4a8e7576c8b290bdc88001f6f(self):
        return re.search(
            self.SPONSOR_PORTAL_cd6793a4a8e7576c8b290bdc88001f6f_PATTERN,
            self.path
        )

    def sponsor_portal_get_sponsor_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SponsorPortal': {'id': 'string', 'name': 'string', 'description': 'string', 'portalType': 'string', 'portalTestUrl': 'string', 'settings': {'portalSettings': {'httpsPort': 0, 'allowedInterfaces': 'string', 'certificateGroupTag': 'string', 'fqdn': 'string', 'authenticationMethod': 'string', 'idleTimeout': 0, 'displayLang': 'string', 'fallbackLanguage': 'string', 'availableSsids': 'string'}, 'loginPageSettings': {'maxFailedAttemptsBeforeRateLimit': 0, 'timeBetweenLoginsDuringRateLimit': 0, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'requireAupScrolling': True, 'socialConfigs': []}, 'aupSettings': {'includeAup': True, 'requireScrolling': True, 'displayFrequency': 'string', 'displayFrequencyIntervalDays': 0}, 'sponsorChangePasswordSettings': {'allowSponsorToChangePwd': True}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'postAccessBannerSettings': {'includePostAccessBanner': True}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string', 'defaultEmptyFieldValue': 'string'}}, 'customizations': {'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'backgroundImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSOR_PORTAL_bd8691c5d9435e48a3c7a08658bda585(self):
        return re.search(
            self.SPONSOR_PORTAL_bd8691c5d9435e48a3c7a08658bda585_PATTERN,
            self.path
        )

    def sponsor_portal_update_sponsor_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSOR_PORTAL_d8d4c7451f7f5e2faae4e8ac530b5f08(self):
        return re.search(
            self.SPONSOR_PORTAL_d8d4c7451f7f5e2faae4e8ac530b5f08_PATTERN,
            self.path
        )

    def sponsor_portal_delete_sponsor_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSOR_PORTAL_69aa24c1260a568b93c283ecd2c3510e(self):
        return re.search(
            self.SPONSOR_PORTAL_69aa24c1260a568b93c283ecd2c3510e_PATTERN,
            self.path
        )

    def sponsor_portal_get_all_sponsor_portal_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSOR_PORTAL_1f15d19b858d59218ab56b7323ca2fae(self):
        return re.search(
            self.SPONSOR_PORTAL_1f15d19b858d59218ab56b7323ca2fae_PATTERN,
            self.path
        )

    def sponsor_portal_create_sponsor_portal_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSOR_PORTAL_fa39b9cc4834522395edcbe0d6830ae4(self):
        return re.search(
            self.SPONSOR_PORTAL_fa39b9cc4834522395edcbe0d6830ae4_PATTERN,
            self.path
        )

    def sponsor_portal_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSORED_GUEST_PORTAL_56d1132a216d54d091022aec0ad018f8(self):
        return re.search(
            self.SPONSORED_GUEST_PORTAL_56d1132a216d54d091022aec0ad018f8_PATTERN,
            self.path
        )

    def sponsored_guest_portal_get_sponsored_guest_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SponsoredGuestPortal': {'id': 'string', 'name': 'string', 'description': 'string', 'portalType': 'string', 'portalTestUrl': 'string', 'settings': {'portalSettings': {'httpsPort': 0, 'allowedInterfaces': 'string', 'certificateGroupTag': 'string', 'authenticationMethod': 'string', 'assignedGuestTypeForEmployee': 'string', 'displayLang': 'string', 'fallbackLanguage': 'string', 'alwaysUsedLanguage': 'string'}, 'loginPageSettings': {'requireAccessCode': True, 'maxFailedAttemptsBeforeRateLimit': 0, 'timeBetweenLoginsDuringRateLimit': 0, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'accessCode': 'string', 'allowGuestToCreateAccounts': True, 'allowForgotPassword': True, 'allowGuestToChangePassword': True, 'allowAlternateGuestPortal': True, 'socialConfigs': [{'socialMediaType': 'string', 'socialMediaValue': 'string'}]}, 'aupSettings': {'includeAup': True, 'requireAupScrolling': True, 'useDiffAupForEmployees': True, 'skipAupForEmployees': True, 'displayFrequencyIntervalDays': 0, 'requireScrolling': True, 'displayFrequency': 'string'}, 'guestChangePasswordSettings': {'allowChangePasswdAtFirstLogin': True}, 'guestDeviceRegistrationSettings': {'autoRegisterGuestDevices': True, 'allowGuestsToRegisterDevices': True}, 'byodSettings': {'byodWelcomeSettings': {'enableBYOD': True, 'enableGuestAccess': True, 'requireMDM': True, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'requireScrolling': True}, 'byodRegistrationSettings': {'showDeviceID': True, 'endPointIdentityGroupId': 'string'}, 'byodRegistrationSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}}, 'postAccessBannerSettings': {'includePostAccessBanner': True}, 'authSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string', 'defaultEmptyFieldValue': 'string'}}, 'customizations': {'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'backgroundImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSORED_GUEST_PORTAL_0d39172f68fd5cbd897f03f1440f98a4(self):
        return re.search(
            self.SPONSORED_GUEST_PORTAL_0d39172f68fd5cbd897f03f1440f98a4_PATTERN,
            self.path
        )

    def sponsored_guest_portal_update_sponsored_guest_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSORED_GUEST_PORTAL_9218749931f05e2ebc796f080892085f(self):
        return re.search(
            self.SPONSORED_GUEST_PORTAL_9218749931f05e2ebc796f080892085f_PATTERN,
            self.path
        )

    def sponsored_guest_portal_delete_sponsored_guest_portal_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSORED_GUEST_PORTAL_97886854bdae59219027b4d40b94fa3d(self):
        return re.search(
            self.SPONSORED_GUEST_PORTAL_97886854bdae59219027b4d40b94fa3d_PATTERN,
            self.path
        )

    def sponsored_guest_portal_get_all_sponsored_guest_portals_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSORED_GUEST_PORTAL_ca78559d8a9f559c87f53ea85169a2c7(self):
        return re.search(
            self.SPONSORED_GUEST_PORTAL_ca78559d8a9f559c87f53ea85169a2c7_PATTERN,
            self.path
        )

    def sponsored_guest_portal_create_sponsored_guest_portal_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SPONSORED_GUEST_PORTAL_2f1aacc5c48654cebbc4d075dc7dde80(self):
        return re.search(
            self.SPONSORED_GUEST_PORTAL_2f1aacc5c48654cebbc4d075dc7dde80_PATTERN,
            self.path
        )

    def sponsored_guest_portal_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_CONNECTIONS_86a5b160a5675039b7ddf3dc960c7968(self):
        return re.search(
            self.SXP_CONNECTIONS_86a5b160a5675039b7ddf3dc960c7968_PATTERN,
            self.path
        )

    def sxp_connections_get_sxp_connections_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSSxpConnection': {'id': 'string', 'description': 'string', 'sxpPeer': 'string', 'sxpVpn': 'string', 'sxpNode': 'string', 'ipAddress': 'string', 'sxpMode': 'string', 'sxpVersion': 'string', 'enabled': True, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_CONNECTIONS_1cab8440e21553c3a807d23d05e5e1aa(self):
        return re.search(
            self.SXP_CONNECTIONS_1cab8440e21553c3a807d23d05e5e1aa_PATTERN,
            self.path
        )

    def sxp_connections_update_sxp_connections_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_CONNECTIONS_65954377fb665776b98ba815b52515a6(self):
        return re.search(
            self.SXP_CONNECTIONS_65954377fb665776b98ba815b52515a6_PATTERN,
            self.path
        )

    def sxp_connections_delete_sxp_connections_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_CONNECTIONS_7c56dfcff6285f9b882c884873d5d6c1(self):
        return re.search(
            self.SXP_CONNECTIONS_7c56dfcff6285f9b882c884873d5d6c1_PATTERN,
            self.path
        )

    def sxp_connections_get_all_sxp_connections_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_CONNECTIONS_789c371214c759f791c0a522b9eaf5b5(self):
        return re.search(
            self.SXP_CONNECTIONS_789c371214c759f791c0a522b9eaf5b5_PATTERN,
            self.path
        )

    def sxp_connections_create_sxp_connections_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_CONNECTIONS_c1ceea62877152f6a4cf7ce709f4d0f8(self):
        return re.search(
            self.SXP_CONNECTIONS_c1ceea62877152f6a4cf7ce709f4d0f8_PATTERN,
            self.path
        )

    def sxp_connections_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_CONNECTIONS_a9d9ce4538605d439015d3ed7ef88c41(self):
        return re.search(
            self.SXP_CONNECTIONS_a9d9ce4538605d439015d3ed7ef88c41_PATTERN,
            self.path
        )

    def sxp_connections_bulk_request_for_sxp_connections_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_CONNECTIONS_9462c2fb20ca5eb79facdda896457507(self):
        return re.search(
            self.SXP_CONNECTIONS_9462c2fb20ca5eb79facdda896457507_PATTERN,
            self.path
        )

    def sxp_connections_monitor_bulk_status_sxp_connections_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'BulkStatus': {'bulkId': 'string', 'mediaType': 'string', 'executionStatus': 'string', 'operationType': 'string', 'startTime': 'string', 'resourcesCount': 0, 'successCount': 0, 'failCount': 0, 'resourcesStatus': [{'id': 'string', 'name': 'string', 'description': 'string', 'resourceExecutionStatus': 'string', 'status': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_LOCAL_BINDINGS_e56bea5248a25f799b02fcb6098a7b10(self):
        return re.search(
            self.SXP_LOCAL_BINDINGS_e56bea5248a25f799b02fcb6098a7b10_PATTERN,
            self.path
        )

    def sxp_local_bindings_get_sxp_local_bindings_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSSxpLocalBindings': {'id': 'string', 'ipAddressOrHost': 'string', 'sxpVpn': 'string', 'sgt': 'string', 'vns': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_LOCAL_BINDINGS_313e07cb8ea65820863cce345c67926b(self):
        return re.search(
            self.SXP_LOCAL_BINDINGS_313e07cb8ea65820863cce345c67926b_PATTERN,
            self.path
        )

    def sxp_local_bindings_update_sxp_local_bindings_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_LOCAL_BINDINGS_77db04edfe595fbba5b49eb71dcb65bd(self):
        return re.search(
            self.SXP_LOCAL_BINDINGS_77db04edfe595fbba5b49eb71dcb65bd_PATTERN,
            self.path
        )

    def sxp_local_bindings_delete_sxp_local_bindings_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_LOCAL_BINDINGS_91f845bd746a5c00967fe66178c5edbf(self):
        return re.search(
            self.SXP_LOCAL_BINDINGS_91f845bd746a5c00967fe66178c5edbf_PATTERN,
            self.path
        )

    def sxp_local_bindings_get_all_sxp_local_bindings_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_LOCAL_BINDINGS_84610cf67e0155eab895b50d1a377f21(self):
        return re.search(
            self.SXP_LOCAL_BINDINGS_84610cf67e0155eab895b50d1a377f21_PATTERN,
            self.path
        )

    def sxp_local_bindings_create_sxp_local_bindings_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_LOCAL_BINDINGS_ee22235f36835dec897ed6381e3e15fc(self):
        return re.search(
            self.SXP_LOCAL_BINDINGS_ee22235f36835dec897ed6381e3e15fc_PATTERN,
            self.path
        )

    def sxp_local_bindings_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_LOCAL_BINDINGS_2b97435f47305f5da136a0d68ac6d466(self):
        return re.search(
            self.SXP_LOCAL_BINDINGS_2b97435f47305f5da136a0d68ac6d466_PATTERN,
            self.path
        )

    def sxp_local_bindings_bulk_request_for_sxp_local_bindings_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_LOCAL_BINDINGS_475db866e1125ca0b7cd7cc13ac4bdd4(self):
        return re.search(
            self.SXP_LOCAL_BINDINGS_475db866e1125ca0b7cd7cc13ac4bdd4_PATTERN,
            self.path
        )

    def sxp_local_bindings_monitor_bulk_status_sxp_local_bindings_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'BulkStatus': {'bulkId': 'string', 'mediaType': 'string', 'executionStatus': 'string', 'operationType': 'string', 'startTime': 'string', 'resourcesCount': 0, 'successCount': 0, 'failCount': 0, 'resourcesStatus': [{'id': 'string', 'name': 'string', 'description': 'string', 'resourceExecutionStatus': 'string', 'status': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_VPNS_cd59f40aa9305587b69944a9c819f7a9(self):
        return re.search(
            self.SXP_VPNS_cd59f40aa9305587b69944a9c819f7a9_PATTERN,
            self.path
        )

    def sxp_vpns_get_sxp_vpn_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'ERSSxpVpn': {'id': 'string', 'sxpVpnName': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_VPNS_8a0501930cc9517ea1cb4103db6e0af7(self):
        return re.search(
            self.SXP_VPNS_8a0501930cc9517ea1cb4103db6e0af7_PATTERN,
            self.path
        )

    def sxp_vpns_delete_sxp_vpn_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_VPNS_2a93d058764b51dc922e41bbe4ff7cd6(self):
        return re.search(
            self.SXP_VPNS_2a93d058764b51dc922e41bbe4ff7cd6_PATTERN,
            self.path
        )

    def sxp_vpns_get_all_sxp_vpns_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_VPNS_1a693347bdd15bb19d69a75f088498ce(self):
        return re.search(
            self.SXP_VPNS_1a693347bdd15bb19d69a75f088498ce_PATTERN,
            self.path
        )

    def sxp_vpns_create_sxp_vpn_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_VPNS_36ca67bf525555b086ecee4cb93e9aee(self):
        return re.search(
            self.SXP_VPNS_36ca67bf525555b086ecee4cb93e9aee_PATTERN,
            self.path
        )

    def sxp_vpns_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_VPNS_be45eed0938a5143bf85ffd5fd4205d0(self):
        return re.search(
            self.SXP_VPNS_be45eed0938a5143bf85ffd5fd4205d0_PATTERN,
            self.path
        )

    def sxp_vpns_bulk_request_for_sxp_vpns_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SXP_VPNS_ba771c958ccc5f499c3a819fb2c67f57(self):
        return re.search(
            self.SXP_VPNS_ba771c958ccc5f499c3a819fb2c67f57_PATTERN,
            self.path
        )

    def sxp_vpns_monitor_bulk_status_sxp_vpns_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'BulkStatus': {'bulkId': 'string', 'mediaType': 'string', 'executionStatus': 'string', 'operationType': 'string', 'startTime': 'string', 'resourcesCount': 0, 'successCount': 0, 'failCount': 0, 'resourcesStatus': [{'id': 'string', 'name': 'string', 'description': 'string', 'resourceExecutionStatus': 'string', 'status': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SYSTEM_CERTIFICATE_dd469dcee9445c72a3861ef94fb3b096(self):
        return re.search(
            self.SYSTEM_CERTIFICATE_dd469dcee9445c72a3861ef94fb3b096_PATTERN,
            self.path
        )

    def system_certificate_create_system_certificate_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SYSTEM_CERTIFICATE_3512a19fb8fe5fe9b069aa19d2dd74d5(self):
        return re.search(
            self.SYSTEM_CERTIFICATE_3512a19fb8fe5fe9b069aa19d2dd74d5_PATTERN,
            self.path
        )

    def system_certificate_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_COMMAND_SETS_34f8ba0e97135ca6bacff94d5a76df97(self):
        return re.search(
            self.TACACS_COMMAND_SETS_34f8ba0e97135ca6bacff94d5a76df97_PATTERN,
            self.path
        )

    def tacacs_command_sets_get_tacacs_command_sets_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'TacacsCommandSets': {'id': 'string', 'name': 'string', 'description': 'string', 'permitUnmatched': True, 'commands': {'commandList': [{'grant': 'string', 'command': 'string', 'arguments': 'string'}]}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_COMMAND_SETS_2caefe2cb042513ab4a4a76f227330cb(self):
        return re.search(
            self.TACACS_COMMAND_SETS_2caefe2cb042513ab4a4a76f227330cb_PATTERN,
            self.path
        )

    def tacacs_command_sets_get_tacacs_command_sets_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'TacacsCommandSets': {'id': 'string', 'name': 'string', 'description': 'string', 'permitUnmatched': True, 'commands': {'commandList': [{'grant': 'string', 'command': 'string', 'arguments': 'string'}]}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_COMMAND_SETS_20eb6323be425816a4116eea48f16f4b(self):
        return re.search(
            self.TACACS_COMMAND_SETS_20eb6323be425816a4116eea48f16f4b_PATTERN,
            self.path
        )

    def tacacs_command_sets_update_tacacs_command_sets_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_COMMAND_SETS_4a319a83b14252eba0f00bb4c4ab0d7c(self):
        return re.search(
            self.TACACS_COMMAND_SETS_4a319a83b14252eba0f00bb4c4ab0d7c_PATTERN,
            self.path
        )

    def tacacs_command_sets_delete_tacacs_command_sets_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_COMMAND_SETS_c9a67d3e9015580f93a52627f19e9916(self):
        return re.search(
            self.TACACS_COMMAND_SETS_c9a67d3e9015580f93a52627f19e9916_PATTERN,
            self.path
        )

    def tacacs_command_sets_get_all_tacacs_command_sets_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_COMMAND_SETS_d9cc879878ee5a34ac1c32f2f0cb8c6d(self):
        return re.search(
            self.TACACS_COMMAND_SETS_d9cc879878ee5a34ac1c32f2f0cb8c6d_PATTERN,
            self.path
        )

    def tacacs_command_sets_create_tacacs_command_sets_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_COMMAND_SETS_5865f0adb7f554eb810687bd8699149a(self):
        return re.search(
            self.TACACS_COMMAND_SETS_5865f0adb7f554eb810687bd8699149a_PATTERN,
            self.path
        )

    def tacacs_command_sets_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_EXTERNAL_SERVERS_afe1108b1a59539ebe3de3e5652c9653(self):
        return re.search(
            self.TACACS_EXTERNAL_SERVERS_afe1108b1a59539ebe3de3e5652c9653_PATTERN,
            self.path
        )

    def tacacs_external_servers_get_tacacs_external_servers_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'TacacsExternalServer': {'id': 'string', 'name': 'string', 'description': 'string', 'hostIP': 'string', 'connectionPort': 0, 'singleConnect': True, 'sharedSecret': 'string', 'timeout': 0, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_EXTERNAL_SERVERS_8b9eb9547216547cab8b9e686eee674b(self):
        return re.search(
            self.TACACS_EXTERNAL_SERVERS_8b9eb9547216547cab8b9e686eee674b_PATTERN,
            self.path
        )

    def tacacs_external_servers_get_tacacs_external_servers_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'TacacsExternalServer': {'id': 'string', 'name': 'string', 'description': 'string', 'hostIP': 'string', 'connectionPort': 0, 'singleConnect': True, 'sharedSecret': 'string', 'timeout': 0, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_EXTERNAL_SERVERS_7a7cffe3bfae55aa81b7b4447519e4cd(self):
        return re.search(
            self.TACACS_EXTERNAL_SERVERS_7a7cffe3bfae55aa81b7b4447519e4cd_PATTERN,
            self.path
        )

    def tacacs_external_servers_update_tacacs_external_servers_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_EXTERNAL_SERVERS_896816622564523798353b885b115048(self):
        return re.search(
            self.TACACS_EXTERNAL_SERVERS_896816622564523798353b885b115048_PATTERN,
            self.path
        )

    def tacacs_external_servers_delete_tacacs_external_servers_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_EXTERNAL_SERVERS_8c6c2a4908ee5f48b7e9cae7572f6a94(self):
        return re.search(
            self.TACACS_EXTERNAL_SERVERS_8c6c2a4908ee5f48b7e9cae7572f6a94_PATTERN,
            self.path
        )

    def tacacs_external_servers_get_all_tacacs_external_servers_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_EXTERNAL_SERVERS_b5097e4db7505ba390914b50b1c2046b(self):
        return re.search(
            self.TACACS_EXTERNAL_SERVERS_b5097e4db7505ba390914b50b1c2046b_PATTERN,
            self.path
        )

    def tacacs_external_servers_create_tacacs_external_servers_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_EXTERNAL_SERVERS_d3e106d187b35547bf1f0463e4fc832f(self):
        return re.search(
            self.TACACS_EXTERNAL_SERVERS_d3e106d187b35547bf1f0463e4fc832f_PATTERN,
            self.path
        )

    def tacacs_external_servers_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_PROFILE_3578b8696d875b12b0a3ab735b397d7a(self):
        return re.search(
            self.TACACS_PROFILE_3578b8696d875b12b0a3ab735b397d7a_PATTERN,
            self.path
        )

    def tacacs_profile_get_tacacs_profile_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'TacacsProfile': {'id': 'string', 'name': 'string', 'description': 'string', 'sessionAttributes': {'sessionAttributeList': [{'type': 'string', 'name': 'string', 'value': 'string'}]}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_PROFILE_bdea52558473565c9963ec14c65727b8(self):
        return re.search(
            self.TACACS_PROFILE_bdea52558473565c9963ec14c65727b8_PATTERN,
            self.path
        )

    def tacacs_profile_get_tacacs_profile_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'TacacsProfile': {'id': 'string', 'name': 'string', 'description': 'string', 'sessionAttributes': {'sessionAttributeList': [{'type': 'string', 'name': 'string', 'value': 'string'}]}, 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_PROFILE_4a0db9ec45c05879a6f016a1edf54793(self):
        return re.search(
            self.TACACS_PROFILE_4a0db9ec45c05879a6f016a1edf54793_PATTERN,
            self.path
        )

    def tacacs_profile_update_tacacs_profile_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_PROFILE_9fd38182c505549fbc0d8c1122c1f685(self):
        return re.search(
            self.TACACS_PROFILE_9fd38182c505549fbc0d8c1122c1f685_PATTERN,
            self.path
        )

    def tacacs_profile_delete_tacacs_profile_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_PROFILE_ffff1c792bf559ebb39b789421be6966(self):
        return re.search(
            self.TACACS_PROFILE_ffff1c792bf559ebb39b789421be6966_PATTERN,
            self.path
        )

    def tacacs_profile_get_all_tacacs_profile_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_PROFILE_c094086382485201ad36d4641fc6822e(self):
        return re.search(
            self.TACACS_PROFILE_c094086382485201ad36d4641fc6822e_PATTERN,
            self.path
        )

    def tacacs_profile_create_tacacs_profile_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_PROFILE_17b22259a4415709a97bd2b7646f734f(self):
        return re.search(
            self.TACACS_PROFILE_17b22259a4415709a97bd2b7646f734f_PATTERN,
            self.path
        )

    def tacacs_profile_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_SERVER_SEQUENCE_493b03900a2e5027b615d9f1bdcf9f63(self):
        return re.search(
            self.TACACS_SERVER_SEQUENCE_493b03900a2e5027b615d9f1bdcf9f63_PATTERN,
            self.path
        )

    def tacacs_server_sequence_get_tacacs_server_sequence_by_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'TacacsServerSequence': {'id': 'string', 'name': 'string', 'description': 'string', 'serverList': 'string', 'localAccounting': True, 'remoteAccounting': True, 'prefixStrip': True, 'prefixDelimiter': 'string', 'suffixStrip': True, 'suffixDelimiter': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_SERVER_SEQUENCE_8b9eb9547216547cab8b9e686eee674b(self):
        return re.search(
            self.TACACS_SERVER_SEQUENCE_8b9eb9547216547cab8b9e686eee674b_PATTERN,
            self.path
        )

    def tacacs_server_sequence_get_tacacs_server_sequence_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'TacacsServerSequence': {'id': 'string', 'name': 'string', 'description': 'string', 'serverList': 'string', 'localAccounting': True, 'remoteAccounting': True, 'prefixStrip': True, 'prefixDelimiter': 'string', 'suffixStrip': True, 'suffixDelimiter': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_SERVER_SEQUENCE_7a7cffe3bfae55aa81b7b4447519e4cd(self):
        return re.search(
            self.TACACS_SERVER_SEQUENCE_7a7cffe3bfae55aa81b7b4447519e4cd_PATTERN,
            self.path
        )

    def tacacs_server_sequence_update_tacacs_server_sequence_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'UpdatedFieldsList': {'updatedField': {'field': 'string', 'oldValue': 'string', 'newValue': 'string'}, 'field': 'string', 'oldValue': 'string', 'newValue': 'string'}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_SERVER_SEQUENCE_896816622564523798353b885b115048(self):
        return re.search(
            self.TACACS_SERVER_SEQUENCE_896816622564523798353b885b115048_PATTERN,
            self.path
        )

    def tacacs_server_sequence_delete_tacacs_server_sequence_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_SERVER_SEQUENCE_54187c189f2f5f6b8bab3931c206c949(self):
        return re.search(
            self.TACACS_SERVER_SEQUENCE_54187c189f2f5f6b8bab3931c206c949_PATTERN,
            self.path
        )

    def tacacs_server_sequence_get_all_tacacs_server_sequence_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'name': 'string', 'description': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_SERVER_SEQUENCE_5902a1e26e595667bd98f84dd29232e2(self):
        return re.search(
            self.TACACS_SERVER_SEQUENCE_5902a1e26e595667bd98f84dd29232e2_PATTERN,
            self.path
        )

    def tacacs_server_sequence_create_tacacs_server_sequence_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TACACS_SERVER_SEQUENCE_aa8e1dc47a445d44ab86020f421ee721(self):
        return re.search(
            self.TACACS_SERVER_SEQUENCE_aa8e1dc47a445d44ab86020f421ee721_PATTERN,
            self.path
        )

    def tacacs_server_sequence_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TELEMETRY_INFORMATION_13891f52605b5f6481f6a99ec8a7e8e6(self):
        return re.search(
            self.TELEMETRY_INFORMATION_13891f52605b5f6481f6a99ec8a7e8e6_PATTERN,
            self.path
        )

    def telemetry_information_get_telemetry_info_by_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'TelemetryInfo': {'id': 'string', 'status': 'string', 'deploymentId': 'string', 'udiSN': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TELEMETRY_INFORMATION_8f1a8ae602c95ac08676391c374274f2(self):
        return re.search(
            self.TELEMETRY_INFORMATION_8f1a8ae602c95ac08676391c374274f2_PATTERN,
            self.path
        )

    def telemetry_information_get_all_telemetry_information_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'SearchResult': {'total': 0, 'resources': [{'id': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}], 'nextPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}], 'previousPage': [{'rel': 'string', 'href': 'string', 'type': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TELEMETRY_INFORMATION_86338cd5bfb6540cb70f4bc100a96aed(self):
        return re.search(
            self.TELEMETRY_INFORMATION_86338cd5bfb6540cb70f4bc100a96aed_PATTERN,
            self.path
        )

    def telemetry_information_get_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'VersionInfo': {'currentServerVersion': 'string', 'supportedVersions': 'string', 'link': {'rel': 'string', 'href': 'string', 'type': 'string'}}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_0e629f554fa652d980ff08988c788c57(self):
        return re.search(
            self.MISC_0e629f554fa652d980ff08988c788c57_PATTERN,
            self.path
        )

    def misc_get_active_count_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'count': 0})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_6a6c71a1e4d2597ea1b5533e9f1b438f(self):
        return re.search(
            self.MISC_6a6c71a1e4d2597ea1b5533e9f1b438f_PATTERN,
            self.path
        )

    def misc_get_active_list_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'noOfActiveSession': 0})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_2d91e71e5b84583fb8ea91fcd9fb6751(self):
        return re.search(
            self.MISC_2d91e71e5b84583fb8ea91fcd9fb6751_PATTERN,
            self.path
        )

    def misc_get_session_auth_list_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'noOfActiveSession': 0})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_83d51ebdbbc75c0f8ed6161ae070a276(self):
        return re.search(
            self.MISC_83d51ebdbbc75c0f8ed6161ae070a276_PATTERN,
            self.path
        )

    def misc_get_posture_count_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'count': 0})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_1bdb77066ba75002bd343de0e9120b86(self):
        return re.search(
            self.MISC_1bdb77066ba75002bd343de0e9120b86_PATTERN,
            self.path
        )

    def misc_get_profiler_count_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'count': 0})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_b93e1accc1f35864b9a5b7bc478c7a7c(self):
        return re.search(
            self.MISC_b93e1accc1f35864b9a5b7bc478c7a7c_PATTERN,
            self.path
        )

    def misc_get_sessions_by_mac_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_8329e037613954b58692d89d64eba681(self):
        return re.search(
            self.MISC_8329e037613954b58692d89d64eba681_PATTERN,
            self.path
        )

    def misc_get_sessions_by_username_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_323fb7171efd5df8a0fe319983882265(self):
        return re.search(
            self.MISC_323fb7171efd5df8a0fe319983882265_PATTERN,
            self.path
        )

    def misc_get_sessions_by_nas_ip_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_123c7f72c6db5ecbb380133c106d0566(self):
        return re.search(
            self.MISC_123c7f72c6db5ecbb380133c106d0566_PATTERN,
            self.path
        )

    def misc_get_sessions_by_endpoint_ip_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_4eb415db854f5b12aa326bde54285c59(self):
        return re.search(
            self.MISC_4eb415db854f5b12aa326bde54285c59_PATTERN,
            self.path
        )

    def misc_get_sessions_by_session_id_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_549bd2a2c3735c6ca7b59c86d428e222(self):
        return re.search(
            self.MISC_549bd2a2c3735c6ca7b59c86d428e222_PATTERN,
            self.path
        )

    def misc_delete_all_sessions_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_fc354ec4d361514a8e949f628f8e5f89(self):
        return re.search(
            self.MISC_fc354ec4d361514a8e949f628f8e5f89_PATTERN,
            self.path
        )

    def misc_get_mnt_version_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'name': 'string', 'version': 'string', 'type_of_node': 0})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_e346dbd9f9df554da3a3bcc06f4e77d5(self):
        return re.search(
            self.MISC_e346dbd9f9df554da3a3bcc06f4e77d5_PATTERN,
            self.path
        )

    def misc_get_failure_reasons_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_8877b26746235997bc32ace7d67d6987(self):
        return re.search(
            self.MISC_8877b26746235997bc32ace7d67d6987_PATTERN,
            self.path
        )

    def misc_get_authentication_status_by_mac_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_7f73477346fb5e7097d915c7f0a99659(self):
        return re.search(
            self.MISC_7f73477346fb5e7097d915c7f0a99659_PATTERN,
            self.path
        )

    def misc_session_reauthentication_by_mac_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_5504a097870d5734861255a347911a24(self):
        return re.search(
            self.MISC_5504a097870d5734861255a347911a24_PATTERN,
            self.path
        )

    def misc_session_disconnect_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MISC_644ab0a3ec0359faa72142f074145f6a(self):
        return re.search(
            self.MISC_644ab0a3ec0359faa72142f074145f6a_PATTERN,
            self.path
        )

    def misc_get_account_status_by_mac_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CONSUMER_91101b93b991556cae0fdd562c5e3f63(self):
        return re.search(
            self.CONSUMER_91101b93b991556cae0fdd562c5e3f63_PATTERN,
            self.path
        )

    def consumer_create_account_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CONSUMER_d1f92a9024975e9dad6114255be546bd(self):
        return re.search(
            self.CONSUMER_d1f92a9024975e9dad6114255be546bd_PATTERN,
            self.path
        )

    def consumer_activate_account_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CONSUMER_98c8ffe8c6095203a83131f49d4c8bb2(self):
        return re.search(
            self.CONSUMER_98c8ffe8c6095203a83131f49d4c8bb2_PATTERN,
            self.path
        )

    def consumer_lookup_service_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_CONSUMER_eaad68e7996c5562901de57bf5a0420a(self):
        return re.search(
            self.CONSUMER_eaad68e7996c5562901de57bf5a0420a_PATTERN,
            self.path
        )

    def consumer_access_secret_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MDM_3f66874f1141550da6104eff5428d37a(self):
        return re.search(
            self.MDM_3f66874f1141550da6104eff5428d37a_PATTERN,
            self.path
        )

    def mdm_get_endpoints_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MDM_6419150c239256209b64afc9e5522e11(self):
        return re.search(
            self.MDM_6419150c239256209b64afc9e5522e11_PATTERN,
            self.path
        )

    def mdm_get_endpoint_by_mac_address_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MDM_0239282311e55709895e677699dfc3f7(self):
        return re.search(
            self.MDM_0239282311e55709895e677699dfc3f7_PATTERN,
            self.path
        )

    def mdm_get_endpoints_by_type_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_MDM_339bf2a72bc05f5aabd3a79a5188d86a(self):
        return re.search(
            self.MDM_339bf2a72bc05f5aabd3a79a5188d86a_PATTERN,
            self.path
        )

    def mdm_get_endpoints_by_os_type_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PROFILER_dac693445cb95c6996cf6c7d85dece35(self):
        return re.search(
            self.PROFILER_dac693445cb95c6996cf6c7d85dece35_PATTERN,
            self.path
        )

    def profiler_get_profiles_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PROVIDER_61c9daa26d4b5b80a41d4b7ff9359380(self):
        return re.search(
            self.PROVIDER_61c9daa26d4b5b80a41d4b7ff9359380_PATTERN,
            self.path
        )

    def provider_register_service_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PROVIDER_b480aaa729e75e3d872d0b30a3f8b804(self):
        return re.search(
            self.PROVIDER_b480aaa729e75e3d872d0b30a3f8b804_PATTERN,
            self.path
        )

    def provider_unregister_service_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PROVIDER_ed4d852c55cd54c480986bec7fd9a8bb(self):
        return re.search(
            self.PROVIDER_ed4d852c55cd54c480986bec7fd9a8bb_PATTERN,
            self.path
        )

    def provider_reregister_service_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_PROVIDER_c9088df384b458c3991fed7f718971d5(self):
        return re.search(
            self.PROVIDER_c9088df384b458c3991fed7f718971d5_PATTERN,
            self.path
        )

    def provider_authorization_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_RADIUS_FAILURE_13a3d2bc1bed5e90b1056649e7703d77(self):
        return re.search(
            self.RADIUS_FAILURE_13a3d2bc1bed5e90b1056649e7703d77_PATTERN,
            self.path
        )

    def radius_failure_get_failures_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SESSION_DIRECTORY_9a86b36d56165904911f133e10d4f955(self):
        return re.search(
            self.SESSION_DIRECTORY_9a86b36d56165904911f133e10d4f955_PATTERN,
            self.path
        )

    def session_directory_get_sessions_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SESSION_DIRECTORY_12d6da2024445b2cb8a146fe19889e71(self):
        return re.search(
            self.SESSION_DIRECTORY_12d6da2024445b2cb8a146fe19889e71_PATTERN,
            self.path
        )

    def session_directory_get_sessions_for_recovery_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SESSION_DIRECTORY_2515a470322e5500949321c2cbc1b9c9(self):
        return re.search(
            self.SESSION_DIRECTORY_2515a470322e5500949321c2cbc1b9c9_PATTERN,
            self.path
        )

    def session_directory_get_session_by_ip_address_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SESSION_DIRECTORY_e564f3d00647543db29d1ca6865bc8d0(self):
        return re.search(
            self.SESSION_DIRECTORY_e564f3d00647543db29d1ca6865bc8d0_PATTERN,
            self.path
        )

    def session_directory_get_session_by_mac_address_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SESSION_DIRECTORY_f8021c1d176c5de9b8b41dcde0f0268e(self):
        return re.search(
            self.SESSION_DIRECTORY_f8021c1d176c5de9b8b41dcde0f0268e_PATTERN,
            self.path
        )

    def session_directory_get_user_groups_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SESSION_DIRECTORY_1f674031faf65cac8e2f5581bdef4788(self):
        return re.search(
            self.SESSION_DIRECTORY_1f674031faf65cac8e2f5581bdef4788_PATTERN,
            self.path
        )

    def session_directory_get_user_group_by_user_name_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SYSTEM_HEALTH_0f67f5c0641d55708b20ffc56f374854(self):
        return re.search(
            self.SYSTEM_HEALTH_0f67f5c0641d55708b20ffc56f374854_PATTERN,
            self.path
        )

    def system_health_get_healths_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_SYSTEM_HEALTH_048aadb0c21d5146a207994d493fe9a5(self):
        return re.search(
            self.SYSTEM_HEALTH_048aadb0c21d5146a207994d493fe9a5_PATTERN,
            self.path
        )

    def system_health_get_performances_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TRUST_SEC_CONFIGURATION_9b5b0eb1671a51758acf5ec364d80738(self):
        return re.search(
            self.TRUST_SEC_CONFIGURATION_9b5b0eb1671a51758acf5ec364d80738_PATTERN,
            self.path
        )

    def trust_sec_configuration_get_security_groups_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TRUST_SEC_CONFIGURATION_02b4aa5797455ee4a27390b77262992d(self):
        return re.search(
            self.TRUST_SEC_CONFIGURATION_02b4aa5797455ee4a27390b77262992d_PATTERN,
            self.path
        )

    def trust_sec_configuration_get_security_group_acls_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TRUST_SEC_CONFIGURATION_3da8b5be1a475510a5aa1593d625ffbb(self):
        return re.search(
            self.TRUST_SEC_CONFIGURATION_3da8b5be1a475510a5aa1593d625ffbb_PATTERN,
            self.path
        )

    def trust_sec_configuration_get_egress_policies_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TRUST_SEC_CONFIGURATION_3f9e6e1c33155fdd9a88f48d093f375b(self):
        return re.search(
            self.TRUST_SEC_CONFIGURATION_3f9e6e1c33155fdd9a88f48d093f375b_PATTERN,
            self.path
        )

    def trust_sec_configuration_get_egress_matrices_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_TRUST_SEC_SXP_900a7bddaf5159e68b2caeb19b9979c4(self):
        return re.search(
            self.TRUST_SEC_SXP_900a7bddaf5159e68b2caeb19b9979c4_PATTERN,
            self.path
        )

    def trust_sec_sxp_get_bindings_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def matches_VERSION_AND_PATCH_edea91f35e90539f87a80eb107e02fff(self):
        return re.search(
            self.VERSION_AND_PATCH_edea91f35e90539f87a80eb107e02fff_PATTERN,
            self.path
        )

    def version_and_patch_get_ise_version_and_patch_response(self):
        # Add response status code.
        self.send_response(requests.codes.ok)
        # Add response headers.
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Accept', 'application/json')
        self.end_headers()
        # Add response content.
        response_content = json.dumps({'OperationResult': {'resultValue': [{'value': 'string', 'name': 'string'}]}})
        self.wfile.write(response_content.encode('utf-8'))
        return

    def do_GET(self):

        if self.matches_TASKS_38eb7df265a55d2cbedb08847549b39a():
            self.tasks_get_task_status_response()
            return

        if self.matches_TASKS_bcee1c9523a45056ab79dc64bdf827fe():
            self.tasks_get_task_status_by_id_response()
            return

        if self.matches_NODE_DEPLOYMENT_fa838e78175e51b4bcfb0821c19b81b7():
            self.node_deployment_get_all_nodes_response()
            return

        if self.matches_NODE_DEPLOYMENT_ae8d7c8f33bb52ceb04880845f2f45ba():
            self.node_deployment_get_node_details_response()
            return

        if self.matches_NODE_GROUP_a0824f9a589c58cd8df522524cb550ad():
            self.node_group_get_node_groups_response()
            return

        if self.matches_NODE_GROUP_64a0aadd33595645bf671efc4912f89a():
            self.node_group_get_node_group_response()
            return

        if self.matches_PAN_HA_02daa171ab765a02a714c48376b3790d():
            self.pan_ha_get_pan_ha_status_response()
            return

        if self.matches_REPLICATION_STATUS_7ae615b5e28c54639f44bd10e5b36601():
            self.replication_status_get_node_replication_status_response()
            return

        if self.matches_BACKUP_AND_RESTORE_b0b71a5f25825202b6cb339ce1a5a8d4():
            self.backup_and_restore_get_last_config_backup_status_response()
            return

        if self.matches_REPOSITORY_a83213678e6b58528986f1219d9f12ce():
            self.repository_get_repositories_response()
            return

        if self.matches_REPOSITORY_8a79dc5595ac51d1970b8d53498d3c32():
            self.repository_get_repository_response()
            return

        if self.matches_REPOSITORY_fc645a4297f55557af8d398f07f6d0a0():
            self.repository_get_repository_files_response()
            return

        if self.matches_ANC_ENDPOINT_5ffbc09a97795b8d872a943895c00345():
            self.anc_endpoint_get_anc_endpoint_by_id_response()
            return

        if self.matches_ANC_ENDPOINT_502e681462295b8b8faea9ce6099ff0c():
            self.anc_endpoint_get_all_anc_endpoint_response()
            return

        if self.matches_ANC_ENDPOINT_d5eb6cea45635ef58f5bc624de004f16():
            self.anc_endpoint_get_version_response()
            return

        if self.matches_ANC_ENDPOINT_0a1c6b9323e55505830673a1819840f3():
            self.anc_endpoint_monitor_bulk_status_anc_endpoint_response()
            return

        if self.matches_ANC_POLICY_983a095b061f564ebba331f66505b0e3():
            self.anc_policy_get_anc_policy_by_name_response()
            return

        if self.matches_ANC_POLICY_f41f77362663580d8cc3e6e88623889d():
            self.anc_policy_get_anc_policy_by_id_response()
            return

        if self.matches_ANC_POLICY_440813c9722c56108cac8ca50bf8f01c():
            self.anc_policy_get_all_anc_policy_response()
            return

        if self.matches_ANC_POLICY_b01a12e2b55e582084fab915465bf962():
            self.anc_policy_get_version_response()
            return

        if self.matches_ANC_POLICY_10023cdff02b5185b9b54c9e58762704():
            self.anc_policy_monitor_bulk_status_anc_policy_response()
            return

        if self.matches_CLEAR_THREATS_AND_VULNERABILITIES_83379c74d24e5ae9bb90f798a190cca3():
            self.clear_threats_and_vulnerabilities_get_version_response()
            return

        if self.matches_NODE_DETAILS_ab48268c76aa598788a5ebc370226f3a():
            self.node_details_get_node_by_name_response()
            return

        if self.matches_NODE_DETAILS_0397bb2e9d6651c7bf18c1b60ff7eb14():
            self.node_details_get_node_by_id_response()
            return

        if self.matches_NODE_DETAILS_775d9b8599f55fc4a1bd9d6ac02619eb():
            self.node_details_get_all_nodes_response()
            return

        if self.matches_NODE_DETAILS_ca9a3d8217d5507aa11020bee82ef228():
            self.node_details_get_version_response()
            return

        if self.matches_PSN_NODE_DETAILS_WITH_RADIUS_SERVICE_ab225d0b2a6c52a99df1f1d8fb6a4dac():
            self.psn_node_details_with_radius_service_get_session_service_node_by_name_response()
            return

        if self.matches_PSN_NODE_DETAILS_WITH_RADIUS_SERVICE_c988bb742d055294b74b4d6916ca1ada():
            self.psn_node_details_with_radius_service_get_session_service_node_by_id_response()
            return

        if self.matches_PSN_NODE_DETAILS_WITH_RADIUS_SERVICE_66dccbf248575cbeb3cd3dda5cdbcf20():
            self.psn_node_details_with_radius_service_get_all_session_service_node_response()
            return

        if self.matches_PSN_NODE_DETAILS_WITH_RADIUS_SERVICE_05c0bfee23f95034842993a83d77c4e4():
            self.psn_node_details_with_radius_service_get_version_response()
            return

        if self.matches_PULL_DEPLOYMENT_INFO_f9159c9f9a1951568daee7080e1dda47():
            self.pull_deployment_info_get_all_deployment_info_response()
            return

        if self.matches_PULL_DEPLOYMENT_INFO_8698cc09209259dcbde7c851b5a6eda6():
            self.pull_deployment_info_get_version_response()
            return

        if self.matches_PX_GRID_NODE_111a9d109aac585a89bdd3fae400064b():
            self.px_grid_node_get_px_grid_node_by_name_response()
            return

        if self.matches_PX_GRID_NODE_d24ade0b53405fbc898cb0cc1ea57fb8():
            self.px_grid_node_get_px_grid_node_by_id_response()
            return

        if self.matches_PX_GRID_NODE_52661028d97156379640002f79b2007c():
            self.px_grid_node_get_all_px_grid_node_response()
            return

        if self.matches_PX_GRID_NODE_73c2962d70ef5964be55cfeae68e5ba6():
            self.px_grid_node_get_version_response()
            return

        if self.matches_SUPPORT_BUNDLE_DOWNLOAD_25c57752629f546fb86e84c59285350f():
            self.support_bundle_download_get_version_response()
            return

        if self.matches_SUPPORT_BUNDLE_STATUS_cec7dc317e875ff0a315a7c0556f9c51():
            self.support_bundle_status_get_support_bundle_status_by_id_response()
            return

        if self.matches_SUPPORT_BUNDLE_STATUS_505300e162f051d58c6ae9d5e3851780():
            self.support_bundle_status_get_all_support_bundle_status_response()
            return

        if self.matches_SUPPORT_BUNDLE_STATUS_7ae30c71acc45385a6b3e9a49a8281a9():
            self.support_bundle_status_get_version_response()
            return

        if self.matches_SUPPORT_BUNDLE_TRIGGER_CONFIGURATION_a2b17c3c4eab52caa2fc7c811965c79d():
            self.support_bundle_trigger_configuration_get_version_response()
            return

        if self.matches_CERTIFICATES_87efa004c89a5b85ad30e0dde622bfaf():
            self.certificates_get_csrs_response()
            return

        if self.matches_CERTIFICATES_0910f99dc34755cf954945d5575e3072():
            self.certificates_export_csr_response()
            return

        if self.matches_CERTIFICATES_5015d080d7635e27aef80f42d20b01c8():
            self.certificates_get_csr_by_id_response()
            return

        if self.matches_CERTIFICATES_c2e43687a3205903a3f60728b87f1865():
            self.certificates_get_system_certificates_response()
            return

        if self.matches_CERTIFICATES_c4e07bc79feb5e19bf6cc60220f47bdf():
            self.certificates_get_system_certificate_by_id_response()
            return

        if self.matches_CERTIFICATES_df7d8ed3e15a5d1587cdd7652efe0104():
            self.certificates_get_trusted_certificates_response()
            return

        if self.matches_CERTIFICATES_5978827945b45792ab0b40c8a2d3392c():
            self.certificates_export_trusted_cert_response()
            return

        if self.matches_CERTIFICATES_bee89e08a5145417989aaf187a6d7b2b():
            self.certificates_get_trusted_certificate_by_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_e8bd869250105a2ba30dd2cb65b0b3f2():
            self.device_administration_authentication_rules_get_device_admin_policy_by_id_authentication_rule_list_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_87d71c8af3b55abb8e5959965baf2043():
            self.device_administration_authentication_rules_get_device_admin_policy_by_id_authentication_rule_by_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_0eb446266e3d54f4a657050d4f9b0bf9():
            self.device_administration_authorization_exception_rules_get_device_admin_policy_by_id_local_exception_rule_list_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_5afaa335e2545c6f8f5530cd5686366a():
            self.device_administration_authorization_exception_rules_get_device_admin_policy_by_id_local_exception_rule_by_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_d407475db88f596390eab0a3e8c1d162():
            self.device_administration_authorization_global_exception_rules_get_device_admin_policy_set_global_exception_rule_list_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_3a3d7e48a50d58a8a5d5720f9d55cf45():
            self.device_administration_authorization_global_exception_rules_get_device_admin_policy_set_global_exception_by_rule_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_4e4ac2543c3b53b5982168169f0b29b4():
            self.device_administration_authorization_rules_get_device_admin_policy_by_id_authorization_rule_list_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_f1d11ab85a0a5597b9513d92a894ef1b():
            self.device_administration_authorization_rules_get_device_admin_policy_by_id_authorization_rule_by_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_COMMAND_SET_273e0977618453b1b00e1c2b4cfa1999():
            self.device_administration_command_set_get_device_admin_command_sets_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_CONDITIONS_fdfa9b301f925a34a848f29f223e5b8d():
            self.device_administration_conditions_get_device_admin_conditions_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_CONDITIONS_316863dcb2ca563999b2d3691e1def79():
            self.device_administration_conditions_get_device_admin_conditions_for_authentication_rule_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_CONDITIONS_e67076b912ef5362949be22842642596():
            self.device_administration_conditions_get_device_admin_conditions_for_authorization_rule_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_CONDITIONS_3d9fe67eb28858609eca3907c8343015():
            self.device_administration_conditions_get_device_admin_condition_by_condition_name_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_CONDITIONS_68b404b307a35c2d9438da695bb49c54():
            self.device_administration_conditions_get_device_admin_conditions_for_policy_set_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_CONDITIONS_27c0cf6ab73353ffa2b6986a9b16c54e():
            self.device_administration_conditions_get_device_admin_condition_by_condition_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_DICTIONARY_ATTRIBUTES_LIST_7f1ff6e8bb2d5c7fbcf39fbadf5da2d5():
            self.device_administration_dictionary_attributes_list_get_device_admin_dictionaries_authentication_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_DICTIONARY_ATTRIBUTES_LIST_6e2f955f29ce511993a189f2d234048d():
            self.device_administration_dictionary_attributes_list_get_device_admin_dictionaries_authorization_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_DICTIONARY_ATTRIBUTES_LIST_892e064032895c8098927d3a39ef6af2():
            self.device_administration_dictionary_attributes_list_get_device_admin_dictionaries_policyset_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_IDENTITY_STORES_7ae7d98a7b185837af8d15ae864616e0():
            self.device_administration_identity_stores_get_device_admin_identity_stores_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_bda58fc63575503b80c024dbe02cf547():
            self.device_administration_network_conditions_get_device_admin_network_conditions_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_a3640f918edb5df99d09001ca9e12688():
            self.device_administration_network_conditions_get_device_admin_network_condition_by_condition_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_POLICY_SET_923587ed5920513e92b1728b824771cc():
            self.device_administration_policy_set_get_device_admin_policy_set_list_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_POLICY_SET_49f36918d98a546ab6ca2618d1844984():
            self.device_administration_policy_set_get_device_admin_policy_set_by_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_PROFILES_8ca669963ed0563e96bb009bf14a417b():
            self.device_administration_profiles_get_device_admin_profiles_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_SERVICE_NAMES_36e8018e15b053f39046b5bec0243d3f():
            self.device_administration_service_names_get_device_admin_service_names_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_816bf923264c53f98d5c347fa50b9c15():
            self.device_administration_time_date_conditions_get_device_admin_time_conditions_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_15ffd94d339a5fea8a4777dccccb926f():
            self.device_administration_time_date_conditions_get_device_admin_time_condition_by_condition_id_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHENTICATION_RULES_7956d836da955609bd9a5243101f3536():
            self.network_access_authentication_rules_get_network_access_policy_by_id_authentication_rule_list_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHENTICATION_RULES_85a98a9a386755939fe1f1633be33689():
            self.network_access_authentication_rules_get_network_access_policy_by_id_authentication_rule_by_id_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_9b2117ae65635dfd9c9d7042eb649261():
            self.network_access_authorization_exception_rules_get_network_access_policy_by_id_local_exception_rule_list_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_d01cc518eafd5daeaf80b7e83f4d6ad1():
            self.network_access_authorization_exception_rules_get_network_access_policy_by_id_local_exception_rule_by_id_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_8de9a19a8393543da5814b1dce75abf6():
            self.network_access_authorization_global_exception_rules_get_network_access_policy_set_global_exception_rule_list_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_9b71b104d553520aafc4ce52b537a482():
            self.network_access_authorization_global_exception_rules_get_network_access_policy_set_global_exception_rule_by_id_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_RULES_565fef1c1b1c53eeb784322caec31573():
            self.network_access_authorization_rules_get_network_access_policy_by_id_authorization_rule_list_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_RULES_b19f79dd969d5444a6ba7b2acbf0f3cf():
            self.network_access_authorization_rules_get_network_access_policy_by_id_authorization_rule_by_id_response()
            return

        if self.matches_NETWORK_ACCESS_CONDITIONS_daaac00241cc57a1a360043cbce63df6():
            self.network_access_conditions_get_network_access_conditions_response()
            return

        if self.matches_NETWORK_ACCESS_CONDITIONS_3a155387e56e5f9ba511dc4e4c9f46b4():
            self.network_access_conditions_get_network_access_conditions_for_authentication_rule_response()
            return

        if self.matches_NETWORK_ACCESS_CONDITIONS_3e196799ee895b3981634d93ec48f58c():
            self.network_access_conditions_get_network_access_conditions_for_authorization_rule_response()
            return

        if self.matches_NETWORK_ACCESS_CONDITIONS_9c98c10af4da50d99fb62c7097f07736():
            self.network_access_conditions_get_network_access_condition_by_condition_name_response()
            return

        if self.matches_NETWORK_ACCESS_CONDITIONS_902bf0cf46ba5b60b00176d2897fc7d3():
            self.network_access_conditions_get_network_access_conditions_for_policy_set_response()
            return

        if self.matches_NETWORK_ACCESS_CONDITIONS_150027701d3053acae2eb596718a9ca3():
            self.network_access_conditions_get_network_access_condition_by_condition_id_response()
            return

        if self.matches_NETWORK_ACCESS_DICTIONARY_1eb2cef3895d5bc68b7a28eca42ef630():
            self.network_access_dictionary_get_network_access_dictionaries_response()
            return

        if self.matches_NETWORK_ACCESS_DICTIONARY_e60234354578568697b6740d08170678():
            self.network_access_dictionary_get_network_access_dictionary_response()
            return

        if self.matches_NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_b47094632edd5daea17c82b5fcd812f5():
            self.network_access_dictionary_attribute_get_network_access_dictionary_attributes_by_dictionary_name_response()
            return

        if self.matches_NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_cb8619385d265527a56dc7a27527f3a1():
            self.network_access_dictionary_attribute_get_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name_response()
            return

        if self.matches_NETWORK_ACCESS_DICTIONARY_ATTRIBUTES_LIST_469345c8455c5c6fac438317f314f407():
            self.network_access_dictionary_attributes_list_get_network_access_dictionaries_authentication_response()
            return

        if self.matches_NETWORK_ACCESS_DICTIONARY_ATTRIBUTES_LIST_e86076c61aa9548dacaf5eb77e98a20c():
            self.network_access_dictionary_attributes_list_get_network_access_dictionaries_authorization_response()
            return

        if self.matches_NETWORK_ACCESS_DICTIONARY_ATTRIBUTES_LIST_5bce945bea7456fd930ee327ece18828():
            self.network_access_dictionary_attributes_list_get_network_access_dictionaries_policyset_response()
            return

        if self.matches_NETWORK_ACCESS_IDENTITY_STORES_4ef75d8c1654508aae4fc2ee9b34fabc():
            self.network_access_identity_stores_get_network_access_identity_stores_response()
            return

        if self.matches_NETWORK_ACCESS_NETWORK_CONDITIONS_da2d8b2763ed53d9bec7f9427c4ce344():
            self.network_access_network_conditions_get_network_access_network_conditions_response()
            return

        if self.matches_NETWORK_ACCESS_NETWORK_CONDITIONS_64faeb3bb3f25787844f6973d5a1658f():
            self.network_access_network_conditions_get_network_access_network_condition_by_condition_id_response()
            return

        if self.matches_NETWORK_ACCESS_POLICY_SET_229b904117c35daf8833398c262c403d():
            self.network_access_policy_set_get_network_access_policy_set_list_response()
            return

        if self.matches_NETWORK_ACCESS_POLICY_SET_1fb3b6363bad54678ae56dc699e8c7e8():
            self.network_access_policy_set_get_network_access_policy_set_by_id_response()
            return

        if self.matches_NETWORK_ACCESS_PROFILES_97b33c6c1bdf5c6b8c63835ce0298418():
            self.network_access_profiles_get_network_access_profiles_response()
            return

        if self.matches_NETWORK_ACCESS_SECURITY_GROUPS_b92977dab6965e1c9fd86b96e4aa7e92():
            self.network_access_security_groups_get_network_access_security_groups_response()
            return

        if self.matches_NETWORK_ACCESS_SERVICE_NAMES_ca8f50a31b325fd281ae7f7b69f31d3f():
            self.network_access_service_names_get_network_access_service_names_response()
            return

        if self.matches_NETWORK_ACCESS_TIME_DATE_CONDITIONS_1533f65d301c5ee3a66ac5220cac3348():
            self.network_access_time_date_conditions_get_network_access_time_conditions_response()
            return

        if self.matches_NETWORK_ACCESS_TIME_DATE_CONDITIONS_e8c39503b29051bea788021a168833da():
            self.network_access_time_date_conditions_get_network_access_time_condition_by_condition_id_response()
            return

        if self.matches_ACI_BINDINGS_3d1448851f0154d0b6e9c856ec6cc6f0():
            self.aci_bindings_get_all_aci_bindings_response()
            return

        if self.matches_ACI_BINDINGS_d74b5214bad656c98f21e4968661c3c0():
            self.aci_bindings_get_version_response()
            return

        if self.matches_ACI_SETTINGS_2ea5c865993b56f48f7f43475294a20c():
            self.aci_settings_get_all_aci_settings_response()
            return

        if self.matches_ACI_SETTINGS_462410ea47f65521bcf0ab949b5d72b5():
            self.aci_settings_get_version_response()
            return

        if self.matches_ACTIVE_DIRECTORY_7c6be021c4ca59e48c97afe218219bb1():
            self.active_directory_get_active_directory_by_name_response()
            return

        if self.matches_ACTIVE_DIRECTORY_15236cfcc7615d0492e2dd1b04dd03a9():
            self.active_directory_get_active_directory_by_id_response()
            return

        if self.matches_ACTIVE_DIRECTORY_c8dbec9679d453f78cb47d894c507a7b():
            self.active_directory_get_all_active_directory_response()
            return

        if self.matches_ACTIVE_DIRECTORY_c2d0923990e35be1882e4dee000254a9():
            self.active_directory_get_version_response()
            return

        if self.matches_ADMIN_USER_adac9b81d9235be3b656acf9436583dd():
            self.admin_user_get_admin_user_by_id_response()
            return

        if self.matches_ADMIN_USER_463a109d72fa5ac0a64d357302f26669():
            self.admin_user_get_all_admin_users_response()
            return

        if self.matches_ADMIN_USER_9535a5edeb5057839d702e0f490dc28f():
            self.admin_user_get_version_response()
            return

        if self.matches_ALLOWED_PROTOCOLS_010ac8c8cb9b5007a1e1a6434a20a881():
            self.allowed_protocols_get_allowed_protocol_by_name_response()
            return

        if self.matches_ALLOWED_PROTOCOLS_696e3ddfddd45e299f14ed194926f8de():
            self.allowed_protocols_get_allowed_protocol_by_id_response()
            return

        if self.matches_ALLOWED_PROTOCOLS_d82fe0f9e4635b74af809beaaf98bd07():
            self.allowed_protocols_get_all_allowed_protocols_response()
            return

        if self.matches_ALLOWED_PROTOCOLS_c0f61393474f5744ab0a263a232d3b96():
            self.allowed_protocols_get_version_response()
            return

        if self.matches_AUTHORIZATION_PROFILE_acf0372068885036baee3c4524638f31():
            self.authorization_profile_get_authorization_profile_by_name_response()
            return

        if self.matches_AUTHORIZATION_PROFILE_a69c7f1ad54e5e9cae1f871e19eed61b():
            self.authorization_profile_get_authorization_profile_by_id_response()
            return

        if self.matches_AUTHORIZATION_PROFILE_2e232c5666ab5ed783588f413c3bc644():
            self.authorization_profile_get_all_authorization_profiles_response()
            return

        if self.matches_AUTHORIZATION_PROFILE_3bee8aa3a03a57a3a5eb1418fe1250b6():
            self.authorization_profile_get_version_response()
            return

        if self.matches_BYOD_PORTAL_effdf30a3e3a5781ba1f5cf833395359():
            self.byod_portal_get_byod_portal_by_id_response()
            return

        if self.matches_BYOD_PORTAL_41a23b580495514394b125800e073c9a():
            self.byod_portal_get_all_byod_portal_response()
            return

        if self.matches_BYOD_PORTAL_c5d2d9d8c20b58049cd3326850f2292f():
            self.byod_portal_get_version_response()
            return

        if self.matches_CERTIFICATE_PROFILE_1d473b3690e951be9375d770225b9657():
            self.certificate_profile_get_certificate_profile_by_name_response()
            return

        if self.matches_CERTIFICATE_PROFILE_d24a3f485ff758d099b1e4713f18f1c1():
            self.certificate_profile_get_certificate_profile_by_id_response()
            return

        if self.matches_CERTIFICATE_PROFILE_3be38700993b5f70acfdc8e44f5558d8():
            self.certificate_profile_get_all_certificate_profile_response()
            return

        if self.matches_CERTIFICATE_PROFILE_8e00be3b97b85829bef60c09eaa922ac():
            self.certificate_profile_get_version_response()
            return

        if self.matches_CERTIFICATE_TEMPLATE_e04f248274ea584aa30857975a28297f():
            self.certificate_template_get_certificate_template_by_name_response()
            return

        if self.matches_CERTIFICATE_TEMPLATE_e9e38cdf5bcb5c018b7f10f1d0864215():
            self.certificate_template_get_certificate_template_by_id_response()
            return

        if self.matches_CERTIFICATE_TEMPLATE_dc1da5c3912a5117878160e27f6b533a():
            self.certificate_template_get_all_certificate_template_response()
            return

        if self.matches_CERTIFICATE_TEMPLATE_3f126f916efd575dbc9acae4ab2a1e4e():
            self.certificate_template_get_version_response()
            return

        if self.matches_DOWNLOADABLE_ACL_dfa8f48210e85715beebb44e62fac408():
            self.downloadable_acl_get_downloadable_acl_by_id_response()
            return

        if self.matches_DOWNLOADABLE_ACL_9191bc200af85d598885a990ff9bcbf8():
            self.downloadable_acl_get_all_downloadable_acl_response()
            return

        if self.matches_DOWNLOADABLE_ACL_d10b7914625e5da0861cbeab4cf6440e():
            self.downloadable_acl_get_version_response()
            return

        if self.matches_EGRESS_MATRIX_CELL_0cdc971b23285b87945021bd5983d1cd():
            self.egress_matrix_cell_get_egress_matrix_cell_by_id_response()
            return

        if self.matches_EGRESS_MATRIX_CELL_c5e52706e7095a81b8d32f3024e01cf6():
            self.egress_matrix_cell_get_all_egress_matrix_cell_response()
            return

        if self.matches_EGRESS_MATRIX_CELL_703c9da5c04b59358ac8bb1034340df4():
            self.egress_matrix_cell_get_version_response()
            return

        if self.matches_EGRESS_MATRIX_CELL_72048face30e52b28c76c1b2574de858():
            self.egress_matrix_cell_monitor_bulk_status_egress_matrix_cell_response()
            return

        if self.matches_ENDPOINT_CERTIFICATE_4c5c84028d8f5c078d8ab37553812d39():
            self.endpoint_certificate_get_version_response()
            return

        if self.matches_ENDPOINT_IDENTITY_GROUP_2590f64c3c08518e9eef83a92d69cde3():
            self.endpoint_identity_group_get_endpoint_group_by_name_response()
            return

        if self.matches_ENDPOINT_IDENTITY_GROUP_5e4bfa620f76545d9887045cd24d99a2():
            self.endpoint_identity_group_get_endpoint_group_by_id_response()
            return

        if self.matches_ENDPOINT_IDENTITY_GROUP_cd429bb8ff3556a796570480f742028b():
            self.endpoint_identity_group_get_all_endpoint_groups_response()
            return

        if self.matches_ENDPOINT_IDENTITY_GROUP_1d553cc3b48d5689ac45a582a5d98f9b():
            self.endpoint_identity_group_get_version_response()
            return

        if self.matches_ENDPOINT_f8a2f0834e625822bed1cb4cf34fde5e():
            self.endpoint_get_rejected_endpoints_response()
            return

        if self.matches_ENDPOINT_7d53842e83f0538cab91e097aa6800ce():
            self.endpoint_get_endpoint_by_name_response()
            return

        if self.matches_ENDPOINT_eb8e0ce63376573995a49178435f7747():
            self.endpoint_get_endpoint_by_id_response()
            return

        if self.matches_ENDPOINT_719765b7f7285d71be4645db91b0fc74():
            self.endpoint_get_all_endpoints_response()
            return

        if self.matches_ENDPOINT_85adcb1d998d54838add3b4d644242af():
            self.endpoint_get_version_response()
            return

        if self.matches_ENDPOINT_5b054a43ba875f0da3da5a7d863f3ef7():
            self.endpoint_monitor_bulk_status_endpoint_response()
            return

        if self.matches_EXTERNAL_RADIUS_SERVER_e6019b6b2b605132b57db142f581e710():
            self.external_radius_server_get_external_radius_server_by_name_response()
            return

        if self.matches_EXTERNAL_RADIUS_SERVER_81735151a93c51c59037ec968625ee45():
            self.external_radius_server_get_external_radius_server_by_id_response()
            return

        if self.matches_EXTERNAL_RADIUS_SERVER_9b641825a9555ecba105cabbdf50fc78():
            self.external_radius_server_get_all_external_radius_server_response()
            return

        if self.matches_EXTERNAL_RADIUS_SERVER_a6c3ffe72746500b88be3a5418ead4ba():
            self.external_radius_server_get_version_response()
            return

        if self.matches_FILTER_POLICY_16555f5d5ab6568d8bf5f9932f7ed7f4():
            self.filter_policy_get_filter_policy_by_id_response()
            return

        if self.matches_FILTER_POLICY_250a599ae00f5e47b9ece23cd3183d1c():
            self.filter_policy_get_all_filter_policy_response()
            return

        if self.matches_FILTER_POLICY_209810ed6cad570d90243b1e0dbbe27b():
            self.filter_policy_get_version_response()
            return

        if self.matches_GUEST_LOCATION_ca2e75fbf5b45ba3b399e5616458b855():
            self.guest_location_get_guest_location_by_id_response()
            return

        if self.matches_GUEST_LOCATION_13ea10f18c3655db84657ad855bf6972():
            self.guest_location_get_all_guest_location_response()
            return

        if self.matches_GUEST_LOCATION_fdfe562af248561f981549b96f8ed397():
            self.guest_location_get_version_response()
            return

        if self.matches_GUEST_SMTP_NOTIFICATION_CONFIGURATION_ca28129793d1569bb50de9f43b0d0ee8():
            self.guest_smtp_notification_configuration_get_guest_smtp_notification_settings_by_id_response()
            return

        if self.matches_GUEST_SMTP_NOTIFICATION_CONFIGURATION_51e4c74e9b4e559e95c73e81183a6c7a():
            self.guest_smtp_notification_configuration_get_all_guest_smtp_notification_settings_response()
            return

        if self.matches_GUEST_SMTP_NOTIFICATION_CONFIGURATION_0a0c0e67aead55a2b4db67e9d068351a():
            self.guest_smtp_notification_configuration_get_version_response()
            return

        if self.matches_GUEST_SSID_d5572c56526151cb8ea42de44b2db52c():
            self.guest_ssid_get_guest_ssid_by_id_response()
            return

        if self.matches_GUEST_SSID_c37778a2faa5552894cc60cec13c56c7():
            self.guest_ssid_get_all_guest_ssid_response()
            return

        if self.matches_GUEST_SSID_b400ebaa2d1f51398d3b32e7a6e4ba35():
            self.guest_ssid_get_version_response()
            return

        if self.matches_GUEST_TYPE_4acb5a41fe395b158a3fe1cda996b0cf():
            self.guest_type_get_guest_type_by_id_response()
            return

        if self.matches_GUEST_TYPE_0f41a1e47105581fabf212f259626903():
            self.guest_type_get_all_guest_type_response()
            return

        if self.matches_GUEST_TYPE_a6bfaedfca185fb7b6a86621e866a5f6():
            self.guest_type_get_version_response()
            return

        if self.matches_GUEST_USER_bcb7ec29968e5d5899df4a90d94ed659():
            self.guest_user_get_guest_user_by_name_response()
            return

        if self.matches_GUEST_USER_2645275c3c7d5a3a83d9f7441972d399():
            self.guest_user_get_guest_user_by_id_response()
            return

        if self.matches_GUEST_USER_1a5abd33eeaa52e39e926472751ef79e():
            self.guest_user_get_all_guest_users_response()
            return

        if self.matches_GUEST_USER_76abe22ea0c45f619731bd568c9f57f4():
            self.guest_user_get_version_response()
            return

        if self.matches_GUEST_USER_e38a1af3ad835636a11375363528fa2e():
            self.guest_user_monitor_bulk_status_guest_user_response()
            return

        if self.matches_HOTSPOT_PORTAL_6cbcecf65a0155fcad602d3ac16531a7():
            self.hotspot_portal_get_hotspot_portal_by_id_response()
            return

        if self.matches_HOTSPOT_PORTAL_d912b1c21e2b5dca8b56332d3a8ad13d():
            self.hotspot_portal_get_all_hotspot_portal_response()
            return

        if self.matches_HOTSPOT_PORTAL_91257d81be4f5a0486cc085499c19b1c():
            self.hotspot_portal_get_version_response()
            return

        if self.matches_IDENTITY_GROUPS_1f18bdd1938755409bf6db6b29e85d3a():
            self.identity_groups_get_identity_group_by_name_response()
            return

        if self.matches_IDENTITY_GROUPS_ca3df31c13b857e6b5dbc8357a8ab010():
            self.identity_groups_get_identity_group_by_id_response()
            return

        if self.matches_IDENTITY_GROUPS_9d904c521059563490c4a93871b33d51():
            self.identity_groups_get_all_identity_groups_response()
            return

        if self.matches_IDENTITY_GROUPS_aab79aee0b455bfea8a6d7c6464a2a09():
            self.identity_groups_get_version_response()
            return

        if self.matches_IDENTITY_SEQUENCE_db686413cf4558188ea60ccc05c3e920():
            self.identity_sequence_get_identity_sequence_by_name_response()
            return

        if self.matches_IDENTITY_SEQUENCE_45cb9345e58f5433ae80f5d8f855978b():
            self.identity_sequence_get_identity_sequence_by_id_response()
            return

        if self.matches_IDENTITY_SEQUENCE_feb30ca768795eed82c118d009d7bcd4():
            self.identity_sequence_get_all_identity_sequence_response()
            return

        if self.matches_IDENTITY_SEQUENCE_dc4c840ad93e53d591ca3a39184e6dde():
            self.identity_sequence_get_version_response()
            return

        if self.matches_INTERNAL_USER_7f403dda9440503191536993f569cc6f():
            self.internal_user_get_internal_user_by_name_response()
            return

        if self.matches_INTERNAL_USER_bacf1abfc35e509183c9a7f055cbbfec():
            self.internal_user_get_internal_user_by_id_response()
            return

        if self.matches_INTERNAL_USER_3ccba98a61555ae495f6a05284e3b5ae():
            self.internal_user_get_all_internal_user_response()
            return

        if self.matches_INTERNAL_USER_2af99828533e58a2b84996b85bacc9ff():
            self.internal_user_get_version_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_GROUP_e56b94dafa5652228fd71abd2b4d6df3():
            self.ip_to_sgt_mapping_group_get_ip_to_sgt_mapping_group_by_id_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_GROUP_680a1544a7125003b7803c0ed383f4bf():
            self.ip_to_sgt_mapping_group_get_all_ip_to_sgt_mapping_group_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_GROUP_14c9a2546739540eb2c1cb7c411836cb():
            self.ip_to_sgt_mapping_group_get_version_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_GROUP_bb5f9095ca7953d3bdb16155e263f25a():
            self.ip_to_sgt_mapping_group_monitor_bulk_status_ip_to_sgt_mapping_group_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_17ddc6729af25f8b8c060b20d09f0057():
            self.ip_to_sgt_mapping_get_ip_to_sgt_mapping_by_id_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_10cd9e91565f5c74b9f32ff0e5be6f17():
            self.ip_to_sgt_mapping_get_all_ip_to_sgt_mapping_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_63042762af0b5041b56b12c5c08cc53e():
            self.ip_to_sgt_mapping_get_version_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_9f36d3f43a6157978ec529318ce506e0():
            self.ip_to_sgt_mapping_monitor_bulk_status_ip_to_sgt_mapping_response()
            return

        if self.matches_MY_DEVICE_PORTAL_4bb3528d280652678f8e211b9e418e66():
            self.my_device_portal_get_my_device_portal_by_id_response()
            return

        if self.matches_MY_DEVICE_PORTAL_90a71ccf29f05ee29af909b07bb9c754():
            self.my_device_portal_get_all_my_device_portal_response()
            return

        if self.matches_MY_DEVICE_PORTAL_5e356376df735e72aa55332951806f42():
            self.my_device_portal_get_version_response()
            return

        if self.matches_NATIVE_SUPPLICANT_PROFILE_5d1b9755414c5dcbb61987b2dd06839a():
            self.native_supplicant_profile_get_native_supplicant_profile_by_id_response()
            return

        if self.matches_NATIVE_SUPPLICANT_PROFILE_6470fa9802505d7bbdf85b951581db47():
            self.native_supplicant_profile_get_all_native_supplicant_profile_response()
            return

        if self.matches_NATIVE_SUPPLICANT_PROFILE_f577c55d36b05178b0275dd88c71e118():
            self.native_supplicant_profile_get_version_response()
            return

        if self.matches_NETWORK_DEVICE_GROUP_e1d938f110e059a5abcb9cc8fb3cbd7c():
            self.network_device_group_get_network_device_group_by_name_response()
            return

        if self.matches_NETWORK_DEVICE_GROUP_a0fdb67d95475cd39382171dec96d6c1():
            self.network_device_group_get_network_device_group_by_id_response()
            return

        if self.matches_NETWORK_DEVICE_GROUP_2a1af553d663556ca429a10ed82effda():
            self.network_device_group_get_all_network_device_group_response()
            return

        if self.matches_NETWORK_DEVICE_GROUP_163f22d64bd4557d856a66ad6599d2d1():
            self.network_device_group_get_version_response()
            return

        if self.matches_NETWORK_DEVICE_54d8610d4a355b63aaaa364447d5fa00():
            self.network_device_get_network_device_by_name_response()
            return

        if self.matches_NETWORK_DEVICE_a4ab683ce53052e089626a096abaf451():
            self.network_device_get_network_device_by_id_response()
            return

        if self.matches_NETWORK_DEVICE_48b986fa0f0d54ef98eb135eeb88808a():
            self.network_device_get_all_network_device_response()
            return

        if self.matches_NETWORK_DEVICE_682601e571185718b6ef6e78bfbfdf68():
            self.network_device_get_version_response()
            return

        if self.matches_NETWORK_DEVICE_1bf96800cc265b5e9e1566ec7088619c():
            self.network_device_monitor_bulk_status_network_device_response()
            return

        if self.matches_PORTAL_GLOBAL_SETTING_0ac243ecb8c157658a4bcfe77a102c14():
            self.portal_global_setting_get_portal_global_setting_by_id_response()
            return

        if self.matches_PORTAL_GLOBAL_SETTING_e9ce4a1e1cf955f098343646760e9d58():
            self.portal_global_setting_get_all_portal_global_settings_response()
            return

        if self.matches_PORTAL_GLOBAL_SETTING_a9a99c0aacce5a8181e2ff79bf99ae20():
            self.portal_global_setting_get_version_response()
            return

        if self.matches_PORTAL_THEME_6e58eabefef15feb880ecfe2906d805f():
            self.portal_theme_get_portal_theme_by_id_response()
            return

        if self.matches_PORTAL_THEME_5ad233598ed75e0c97ddd3c3f1af50e4():
            self.portal_theme_get_all_portal_themes_response()
            return

        if self.matches_PORTAL_THEME_b6bf4f02759a5e7f968896a30575e4c6():
            self.portal_theme_get_version_response()
            return

        if self.matches_PORTAL_5ce70db7732c596aa82bd7d1725ac02d():
            self.portal_get_portal_by_id_response()
            return

        if self.matches_PORTAL_2a72ae8af1075d0c94912b008003b13e():
            self.portal_get_all_portals_response()
            return

        if self.matches_PORTAL_1d754ad0697d54c98c2690c5043e0be6():
            self.portal_get_version_response()
            return

        if self.matches_PROFILER_PROFILE_0e176356698b5ec49609504a530c1d8a():
            self.profiler_profile_get_profiler_profile_by_id_response()
            return

        if self.matches_PROFILER_PROFILE_688d53f6d85a5d609d49bd38cfd65e57():
            self.profiler_profile_get_all_profiler_profiles_response()
            return

        if self.matches_PROFILER_PROFILE_de35c041dc1456cca42b7b2e32a4713d():
            self.profiler_profile_get_version_response()
            return

        if self.matches_PX_GRID_SETTINGS_bea00c7a4f9b5e1798ea078e123ff016():
            self.px_grid_settings_get_version_response()
            return

        if self.matches_RADIUS_SERVER_SEQUENCE_0d1df0e230765104863b8d63d5beb68e():
            self.radius_server_sequence_get_radius_server_sequence_by_id_response()
            return

        if self.matches_RADIUS_SERVER_SEQUENCE_c6c330dace185a548f70f4e5d67776ea():
            self.radius_server_sequence_get_all_radius_server_sequence_response()
            return

        if self.matches_RADIUS_SERVER_SEQUENCE_8fb1a72ded19590fa0aa85fc59ea8cfc():
            self.radius_server_sequence_get_version_response()
            return

        if self.matches_RESTID_STORE_17a5f22fc961547f93976a53949cac73():
            self.restid_store_get_rest_id_store_by_name_response()
            return

        if self.matches_RESTID_STORE_788cba3f7ace597da668acfbe00364be():
            self.restid_store_get_rest_id_store_by_id_response()
            return

        if self.matches_RESTID_STORE_d810359e31e453ac8145981b7d5bb7e4():
            self.restid_store_get_all_rest_id_store_response()
            return

        if self.matches_RESTID_STORE_1b8c3846fcf751e4b008eb0a011dea4d():
            self.restid_store_get_version_response()
            return

        if self.matches_SECURITY_GROUPS_ACLS_a50d1bd34d5f593aadf8eb02083c67b0():
            self.security_groups_acls_get_security_groups_acl_by_id_response()
            return

        if self.matches_SECURITY_GROUPS_ACLS_999b22d6ad9f595ab7e3eee5cf44de8a():
            self.security_groups_acls_get_all_security_groups_acl_response()
            return

        if self.matches_SECURITY_GROUPS_ACLS_6704e67a1131578aa794d8377da9a1de():
            self.security_groups_acls_get_version_response()
            return

        if self.matches_SECURITY_GROUPS_ACLS_07af5ee576605a5a915d888924c1e804():
            self.security_groups_acls_monitor_bulk_status_security_groups_acl_response()
            return

        if self.matches_SECURITY_GROUP_TO_VIRTUAL_NETWORK_2112393ea0a65da3ae0346b912a9efac():
            self.security_group_to_virtual_network_get_security_groups_to_vn_to_vlan_by_id_response()
            return

        if self.matches_SECURITY_GROUP_TO_VIRTUAL_NETWORK_e51b6e745cdb5bdda4de26a27b8d92bb():
            self.security_group_to_virtual_network_get_all_security_groups_to_vn_to_vlan_response()
            return

        if self.matches_SECURITY_GROUP_TO_VIRTUAL_NETWORK_7b2811387f4e55c8839c94ea241a3236():
            self.security_group_to_virtual_network_get_version_response()
            return

        if self.matches_SECURITY_GROUP_TO_VIRTUAL_NETWORK_10ea793a0b1b5ac498f7bc74a0aba257():
            self.security_group_to_virtual_network_monitor_bulk_status_security_groups_to_vn_to_vlan_response()
            return

        if self.matches_SECURITY_GROUPS_ea658190e73c5ce1b27e7def4aea28e3():
            self.security_groups_get_security_group_by_id_response()
            return

        if self.matches_SECURITY_GROUPS_b3c356cfc48a5da4b13b8ecbae5748b7():
            self.security_groups_get_all_security_groups_response()
            return

        if self.matches_SECURITY_GROUPS_ad87f41ef4845f19a19bfadac0928ae6():
            self.security_groups_get_version_response()
            return

        if self.matches_SECURITY_GROUPS_a3148b789a935070b99caed1e99592cf():
            self.security_groups_monitor_bulk_status_security_group_response()
            return

        if self.matches_SELF_REGISTERED_PORTAL_f9c9a5e917af53dbbb91733e82e72ebe():
            self.self_registered_portal_get_self_registered_portal_by_id_response()
            return

        if self.matches_SELF_REGISTERED_PORTAL_bb165bd00a6653ac9da440f23ee62ecc():
            self.self_registered_portal_get_all_self_registered_portals_response()
            return

        if self.matches_SELF_REGISTERED_PORTAL_3d8cc0e6962558c58d263f53b857cff0():
            self.self_registered_portal_get_version_response()
            return

        if self.matches_SMS_PROVIDER_17daac88943a5cd2bd745c483448e231():
            self.sms_provider_get_all_sms_provider_response()
            return

        if self.matches_SMS_PROVIDER_37250017e20e5400a53280d52487ecd6():
            self.sms_provider_get_version_response()
            return

        if self.matches_SPONSOR_GROUP_MEMBER_020659d6b1385f4cb9381c13a1fa4356():
            self.sponsor_group_member_get_all_sponsor_group_member_response()
            return

        if self.matches_SPONSOR_GROUP_MEMBER_0f7c916a2e265c11b8b8535e8f88c7d1():
            self.sponsor_group_member_get_version_response()
            return

        if self.matches_SPONSOR_GROUP_eaa0d7c339d152b688876c2e10f51fe7():
            self.sponsor_group_get_sponsor_group_by_id_response()
            return

        if self.matches_SPONSOR_GROUP_f1196f1f6fde5978b0522f096926d443():
            self.sponsor_group_get_all_sponsor_group_response()
            return

        if self.matches_SPONSOR_GROUP_e8d4001b740751e08cfc19e1fdc5fddf():
            self.sponsor_group_get_version_response()
            return

        if self.matches_SPONSOR_PORTAL_cd6793a4a8e7576c8b290bdc88001f6f():
            self.sponsor_portal_get_sponsor_portal_by_id_response()
            return

        if self.matches_SPONSOR_PORTAL_69aa24c1260a568b93c283ecd2c3510e():
            self.sponsor_portal_get_all_sponsor_portal_response()
            return

        if self.matches_SPONSOR_PORTAL_fa39b9cc4834522395edcbe0d6830ae4():
            self.sponsor_portal_get_version_response()
            return

        if self.matches_SPONSORED_GUEST_PORTAL_56d1132a216d54d091022aec0ad018f8():
            self.sponsored_guest_portal_get_sponsored_guest_portal_by_id_response()
            return

        if self.matches_SPONSORED_GUEST_PORTAL_97886854bdae59219027b4d40b94fa3d():
            self.sponsored_guest_portal_get_all_sponsored_guest_portals_response()
            return

        if self.matches_SPONSORED_GUEST_PORTAL_2f1aacc5c48654cebbc4d075dc7dde80():
            self.sponsored_guest_portal_get_version_response()
            return

        if self.matches_SXP_CONNECTIONS_86a5b160a5675039b7ddf3dc960c7968():
            self.sxp_connections_get_sxp_connections_by_id_response()
            return

        if self.matches_SXP_CONNECTIONS_7c56dfcff6285f9b882c884873d5d6c1():
            self.sxp_connections_get_all_sxp_connections_response()
            return

        if self.matches_SXP_CONNECTIONS_c1ceea62877152f6a4cf7ce709f4d0f8():
            self.sxp_connections_get_version_response()
            return

        if self.matches_SXP_CONNECTIONS_9462c2fb20ca5eb79facdda896457507():
            self.sxp_connections_monitor_bulk_status_sxp_connections_response()
            return

        if self.matches_SXP_LOCAL_BINDINGS_e56bea5248a25f799b02fcb6098a7b10():
            self.sxp_local_bindings_get_sxp_local_bindings_by_id_response()
            return

        if self.matches_SXP_LOCAL_BINDINGS_91f845bd746a5c00967fe66178c5edbf():
            self.sxp_local_bindings_get_all_sxp_local_bindings_response()
            return

        if self.matches_SXP_LOCAL_BINDINGS_ee22235f36835dec897ed6381e3e15fc():
            self.sxp_local_bindings_get_version_response()
            return

        if self.matches_SXP_LOCAL_BINDINGS_475db866e1125ca0b7cd7cc13ac4bdd4():
            self.sxp_local_bindings_monitor_bulk_status_sxp_local_bindings_response()
            return

        if self.matches_SXP_VPNS_cd59f40aa9305587b69944a9c819f7a9():
            self.sxp_vpns_get_sxp_vpn_by_id_response()
            return

        if self.matches_SXP_VPNS_2a93d058764b51dc922e41bbe4ff7cd6():
            self.sxp_vpns_get_all_sxp_vpns_response()
            return

        if self.matches_SXP_VPNS_36ca67bf525555b086ecee4cb93e9aee():
            self.sxp_vpns_get_version_response()
            return

        if self.matches_SXP_VPNS_ba771c958ccc5f499c3a819fb2c67f57():
            self.sxp_vpns_monitor_bulk_status_sxp_vpns_response()
            return

        if self.matches_SYSTEM_CERTIFICATE_3512a19fb8fe5fe9b069aa19d2dd74d5():
            self.system_certificate_get_version_response()
            return

        if self.matches_TACACS_COMMAND_SETS_34f8ba0e97135ca6bacff94d5a76df97():
            self.tacacs_command_sets_get_tacacs_command_sets_by_name_response()
            return

        if self.matches_TACACS_COMMAND_SETS_2caefe2cb042513ab4a4a76f227330cb():
            self.tacacs_command_sets_get_tacacs_command_sets_by_id_response()
            return

        if self.matches_TACACS_COMMAND_SETS_c9a67d3e9015580f93a52627f19e9916():
            self.tacacs_command_sets_get_all_tacacs_command_sets_response()
            return

        if self.matches_TACACS_COMMAND_SETS_5865f0adb7f554eb810687bd8699149a():
            self.tacacs_command_sets_get_version_response()
            return

        if self.matches_TACACS_EXTERNAL_SERVERS_afe1108b1a59539ebe3de3e5652c9653():
            self.tacacs_external_servers_get_tacacs_external_servers_by_name_response()
            return

        if self.matches_TACACS_EXTERNAL_SERVERS_8b9eb9547216547cab8b9e686eee674b():
            self.tacacs_external_servers_get_tacacs_external_servers_by_id_response()
            return

        if self.matches_TACACS_EXTERNAL_SERVERS_8c6c2a4908ee5f48b7e9cae7572f6a94():
            self.tacacs_external_servers_get_all_tacacs_external_servers_response()
            return

        if self.matches_TACACS_EXTERNAL_SERVERS_d3e106d187b35547bf1f0463e4fc832f():
            self.tacacs_external_servers_get_version_response()
            return

        if self.matches_TACACS_PROFILE_3578b8696d875b12b0a3ab735b397d7a():
            self.tacacs_profile_get_tacacs_profile_by_name_response()
            return

        if self.matches_TACACS_PROFILE_bdea52558473565c9963ec14c65727b8():
            self.tacacs_profile_get_tacacs_profile_by_id_response()
            return

        if self.matches_TACACS_PROFILE_ffff1c792bf559ebb39b789421be6966():
            self.tacacs_profile_get_all_tacacs_profile_response()
            return

        if self.matches_TACACS_PROFILE_17b22259a4415709a97bd2b7646f734f():
            self.tacacs_profile_get_version_response()
            return

        if self.matches_TACACS_SERVER_SEQUENCE_493b03900a2e5027b615d9f1bdcf9f63():
            self.tacacs_server_sequence_get_tacacs_server_sequence_by_name_response()
            return

        if self.matches_TACACS_SERVER_SEQUENCE_8b9eb9547216547cab8b9e686eee674b():
            self.tacacs_server_sequence_get_tacacs_server_sequence_by_id_response()
            return

        if self.matches_TACACS_SERVER_SEQUENCE_54187c189f2f5f6b8bab3931c206c949():
            self.tacacs_server_sequence_get_all_tacacs_server_sequence_response()
            return

        if self.matches_TACACS_SERVER_SEQUENCE_aa8e1dc47a445d44ab86020f421ee721():
            self.tacacs_server_sequence_get_version_response()
            return

        if self.matches_TELEMETRY_INFORMATION_13891f52605b5f6481f6a99ec8a7e8e6():
            self.telemetry_information_get_telemetry_info_by_id_response()
            return

        if self.matches_TELEMETRY_INFORMATION_8f1a8ae602c95ac08676391c374274f2():
            self.telemetry_information_get_all_telemetry_information_response()
            return

        if self.matches_TELEMETRY_INFORMATION_86338cd5bfb6540cb70f4bc100a96aed():
            self.telemetry_information_get_version_response()
            return

        if self.matches_MISC_0e629f554fa652d980ff08988c788c57():
            self.misc_get_active_count_response()
            return

        if self.matches_MISC_6a6c71a1e4d2597ea1b5533e9f1b438f():
            self.misc_get_active_list_response()
            return

        if self.matches_MISC_2d91e71e5b84583fb8ea91fcd9fb6751():
            self.misc_get_session_auth_list_response()
            return

        if self.matches_MISC_83d51ebdbbc75c0f8ed6161ae070a276():
            self.misc_get_posture_count_response()
            return

        if self.matches_MISC_1bdb77066ba75002bd343de0e9120b86():
            self.misc_get_profiler_count_response()
            return

        if self.matches_MISC_b93e1accc1f35864b9a5b7bc478c7a7c():
            self.misc_get_sessions_by_mac_response()
            return

        if self.matches_MISC_8329e037613954b58692d89d64eba681():
            self.misc_get_sessions_by_username_response()
            return

        if self.matches_MISC_323fb7171efd5df8a0fe319983882265():
            self.misc_get_sessions_by_nas_ip_response()
            return

        if self.matches_MISC_123c7f72c6db5ecbb380133c106d0566():
            self.misc_get_sessions_by_endpoint_ip_response()
            return

        if self.matches_MISC_4eb415db854f5b12aa326bde54285c59():
            self.misc_get_sessions_by_session_id_response()
            return

        if self.matches_MISC_fc354ec4d361514a8e949f628f8e5f89():
            self.misc_get_mnt_version_response()
            return

        if self.matches_MISC_e346dbd9f9df554da3a3bcc06f4e77d5():
            self.misc_get_failure_reasons_response()
            return

        if self.matches_MISC_8877b26746235997bc32ace7d67d6987():
            self.misc_get_authentication_status_by_mac_response()
            return

        if self.matches_MISC_7f73477346fb5e7097d915c7f0a99659():
            self.misc_session_reauthentication_by_mac_response()
            return

        if self.matches_MISC_5504a097870d5734861255a347911a24():
            self.misc_session_disconnect_response()
            return

        if self.matches_MISC_644ab0a3ec0359faa72142f074145f6a():
            self.misc_get_account_status_by_mac_response()
            return

        if self.matches_RADIUS_FAILURE_13a3d2bc1bed5e90b1056649e7703d77():
            self.radius_failure_get_failures_response()
            return

        if self.matches_VERSION_AND_PATCH_edea91f35e90539f87a80eb107e02fff():
            self.version_and_patch_get_ise_version_and_patch_response()
            return

    def do_POST(self):

        if self.matches_NODE_DEPLOYMENT_e82e46732de25832a543c4640312588c():
            self.node_deployment_register_node_response()
            return

        if self.matches_NODE_GROUP_f41d844dbee15f7680920652004f69b6():
            self.node_group_create_node_group_response()
            return

        if self.matches_PAN_HA_fc9a4ee495785518bd2251b6b4fb41f4():
            self.pan_ha_enable_pan_ha_response()
            return

        if self.matches_SYNC_ISE_NODE_582ad69fa1d850f4993bbfc888749fa0():
            self.sync_ise_node_sync_node_response()
            return

        if self.matches_BACKUP_AND_RESTORE_b9638a67f60d5a6aa476af13632d96bd():
            self.backup_and_restore_config_backup_response()
            return

        if self.matches_BACKUP_AND_RESTORE_39527e9813ff50a9bcbbd5d539ed19d8():
            self.backup_and_restore_cancel_backup_response()
            return

        if self.matches_BACKUP_AND_RESTORE_db3505847b4e5f37a5c74bc41df54be3():
            self.backup_and_restore_restore_config_backup_response()
            return

        if self.matches_BACKUP_AND_RESTORE_dd4581dd32f65e8c83cca2f0a97af3e2():
            self.backup_and_restore_create_scheduled_config_backup_response()
            return

        if self.matches_REPOSITORY_17edcb0e8c6b54709d4d61ea23b45f84():
            self.repository_create_repository_response()
            return

        if self.matches_ANC_POLICY_2acfdb4060de5a1895b383238c205986():
            self.anc_policy_create_anc_policy_response()
            return

        if self.matches_SUPPORT_BUNDLE_TRIGGER_CONFIGURATION_492171fac48e5c63abfe2feec6fd1903():
            self.support_bundle_trigger_configuration_create_support_bundle_response()
            return

        if self.matches_CERTIFICATES_dd7a13ef2dea5b9fa6c4d67839133bbf():
            self.certificates_generate_csr_response()
            return

        if self.matches_CERTIFICATES_db47e53374a85830af220e5f982d10da():
            self.certificates_generate_intermediate_ca_csr_response()
            return

        if self.matches_CERTIFICATES_7222975970e85c38bcad4249948c550b():
            self.certificates_regenerate_ise_root_ca_response()
            return

        if self.matches_CERTIFICATES_ce788c3408de5056a2e71955f86d6f05():
            self.certificates_renew_certs_response()
            return

        if self.matches_CERTIFICATES_77c39f0f97cb53e19a03f2ea53f5b831():
            self.certificates_bind_csr_response()
            return

        if self.matches_CERTIFICATES_da5ac537bf475538b7bc42c8cce2e530():
            self.certificates_export_system_cert_response()
            return

        if self.matches_CERTIFICATES_adde5bf7c9185218b955ff0c365fcc4c():
            self.certificates_import_system_cert_response()
            return

        if self.matches_CERTIFICATES_f385b6330ef6500cb599f55407695a3e():
            self.certificates_import_trust_cert_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_73164e92c5af5344b4d9fdc45a282ce5():
            self.device_administration_authentication_rules_create_device_admin_policy_by_id_authentication_rule_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_573a1a3596305814bab0a6d05cf86280():
            self.device_administration_authentication_rules_reset_hit_counts_device_admin_policy_by_id_authentication_rules_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_c730e85640aa5a59bc0e0fd95dacf889():
            self.device_administration_authorization_exception_rules_create_device_admin_policy_by_id_local_exception_rule_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_2dde23cf27e65a60a949d8f1f599b3d2():
            self.device_administration_authorization_exception_rules_reset_hit_counts_device_admin_policy_by_id_local_exceptions_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_8558ade26d445251a45cc753f68d21bc():
            self.device_administration_authorization_global_exception_rules_create_device_admin_policy_set_global_exception_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_6b273ca0ffac58c3921f658152c03dbb():
            self.device_administration_authorization_global_exception_rules_reset_hit_counts_device_admin_global_exceptions_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_8440a5fd2b5d5306b9941387f400c7a0():
            self.device_administration_authorization_rules_create_device_admin_policy_by_id_authorization_rule_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_38edb17577d9503ba1155c2916dcf663():
            self.device_administration_authorization_rules_reset_hit_counts_device_admin_policy_by_id_authorization_rules_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_CONDITIONS_b84dbd77c49f5056b9bf3c1e496ebe5f():
            self.device_administration_conditions_post_device_admin_condition_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_83ea4e38c44e5b1c90b19af25b88546e():
            self.device_administration_network_conditions_post_device_admin_network_condition_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_POLICY_SET_5767ac3ccf225801ad8ba0bb1ad9de0b():
            self.device_administration_policy_set_create_device_admin_policy_set_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_POLICY_SET_ed47964d442d52dca1f7da967f37b3e2():
            self.device_administration_policy_set_reset_hit_counts_device_admin_policy_sets_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_98b30f809e275589bd7154b5b4093d3f():
            self.device_administration_time_date_conditions_post_device_admin_time_condition_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHENTICATION_RULES_c26e318c3c405713a55b4e162be8c890():
            self.network_access_authentication_rules_create_network_access_policy_by_id_authentication_rule_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHENTICATION_RULES_362ffc5178ed53749ebcaadd1c2af785():
            self.network_access_authentication_rules_reset_hit_counts_network_access_policy_by_id_authentication_rules_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_2d40ae38628c51c49af42a4ede3d66d9():
            self.network_access_authorization_exception_rules_create_network_access_policy_by_id_local_exception_rule_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_7d45668b438c59a6b92eb3c79386935b():
            self.network_access_authorization_exception_rules_reset_hit_counts_network_access_policy_by_id_local_exceptions_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_f9df6a3c6cf953319db3b8c36720997d():
            self.network_access_authorization_global_exception_rules_create_network_access_policy_set_global_exception_rule_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_31254fb8a2895e8982180d5f9339f8e4():
            self.network_access_authorization_global_exception_rules_reset_hit_counts_network_access_global_exceptions_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_RULES_b9de636ff2e25f849f468556c53b7b9a():
            self.network_access_authorization_rules_create_network_access_policy_by_id_authorization_rule_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_RULES_e263dfc3d6e5513fa6ae916a22d14e5d():
            self.network_access_authorization_rules_reset_hit_counts_network_access_policy_by_id_authorization_rules_response()
            return

        if self.matches_NETWORK_ACCESS_CONDITIONS_36e5dd2909045a90bdce4848865662c2():
            self.network_access_conditions_post_network_access_condition_response()
            return

        if self.matches_NETWORK_ACCESS_DICTIONARY_7205be755dae5251bd2d8348eeebfdde():
            self.network_access_dictionary_post_network_access_dictionaries_response()
            return

        if self.matches_NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_9d3034483aaa5563bb287ef0cd502130():
            self.network_access_dictionary_attribute_post_network_access_dictionaries_by_dictionary_name_attribute_response()
            return

        if self.matches_NETWORK_ACCESS_NETWORK_CONDITIONS_858ad86a47e15d45ab1cc0cadc5b248f():
            self.network_access_network_conditions_post_network_access_network_condition_response()
            return

        if self.matches_NETWORK_ACCESS_POLICY_SET_42e1af4e392c5790a01685b9687208c0():
            self.network_access_policy_set_create_network_access_policy_set_response()
            return

        if self.matches_NETWORK_ACCESS_POLICY_SET_678aef73e11e56edb468869d663b5e85():
            self.network_access_policy_set_reset_hit_counts_network_access_policy_sets_response()
            return

        if self.matches_NETWORK_ACCESS_TIME_DATE_CONDITIONS_fc5800b01699562cb563664affdd7757():
            self.network_access_time_date_conditions_post_network_access_time_condition_response()
            return

        if self.matches_ACTIVE_DIRECTORY_64e9318040a456978757d7abfa3e66b1():
            self.active_directory_create_active_directory_response()
            return

        if self.matches_ALLOWED_PROTOCOLS_1b40ad23ab0a5a7b8adade320c8912e7():
            self.allowed_protocols_create_allowed_protocol_response()
            return

        if self.matches_AUTHORIZATION_PROFILE_9c43118f80d4556a8ec759a8c41e2097():
            self.authorization_profile_create_authorization_profile_response()
            return

        if self.matches_BYOD_PORTAL_afcce33ec863567f94f3b9b73719ff8d():
            self.byod_portal_create_byod_portal_response()
            return

        if self.matches_CERTIFICATE_PROFILE_776141419f955525b0b38a57a3bed311():
            self.certificate_profile_create_certificate_profile_response()
            return

        if self.matches_DOWNLOADABLE_ACL_adcf947c42fe5588b7b82d9c43a3bbf0():
            self.downloadable_acl_create_downloadable_acl_response()
            return

        if self.matches_EGRESS_MATRIX_CELL_64c560004d8b5f64a10f2cc070368c12():
            self.egress_matrix_cell_create_egress_matrix_cell_response()
            return

        if self.matches_ENDPOINT_IDENTITY_GROUP_b14d63c641e95ac0a8c2da2fb65909c7():
            self.endpoint_identity_group_create_endpoint_group_response()
            return

        if self.matches_ENDPOINT_845787ab88be5092bf4ba9f522e8e26f():
            self.endpoint_create_endpoint_response()
            return

        if self.matches_EXTERNAL_RADIUS_SERVER_1fc1c74b35ae5050b4f7fd702570ad5b():
            self.external_radius_server_create_external_radius_server_response()
            return

        if self.matches_FILTER_POLICY_22f8082b07ce528f82545e210b84d7de():
            self.filter_policy_create_filter_policy_response()
            return

        if self.matches_GUEST_SMTP_NOTIFICATION_CONFIGURATION_01643de7c6f75f68b0d7df00dc72808d():
            self.guest_smtp_notification_configuration_create_guest_smtp_notification_settings_response()
            return

        if self.matches_GUEST_SSID_2a31eb33e3535754b3f754a9199e0d25():
            self.guest_ssid_create_guest_ssid_response()
            return

        if self.matches_GUEST_TYPE_f46c01449d585b088490c4db530c56d5():
            self.guest_type_create_guest_type_response()
            return

        if self.matches_GUEST_USER_89f7cf06a1655d6da606ace9b0950bcf():
            self.guest_user_create_guest_user_response()
            return

        if self.matches_HOTSPOT_PORTAL_0df78c9a3f72584dbd1c7b667b0e312f():
            self.hotspot_portal_create_hotspot_portal_response()
            return

        if self.matches_IDENTITY_GROUPS_592250bf19f653f9a5c48d1fb1890409():
            self.identity_groups_create_identity_group_response()
            return

        if self.matches_IDENTITY_SEQUENCE_6cc0a87094bf5d96af61403dfc3747db():
            self.identity_sequence_create_identity_sequence_response()
            return

        if self.matches_INTERNAL_USER_bf175c04fcb051b9a6fd70a2252903fa():
            self.internal_user_create_internal_user_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_GROUP_55c2e3af6da356009f6499f00a4115e9():
            self.ip_to_sgt_mapping_group_create_ip_to_sgt_mapping_group_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_52dd838b268f5dd298a123ac58448ea9():
            self.ip_to_sgt_mapping_create_ip_to_sgt_mapping_response()
            return

        if self.matches_MY_DEVICE_PORTAL_e643a5ac8bca55f58ea8d6260c57eafe():
            self.my_device_portal_create_my_device_portal_response()
            return

        if self.matches_NETWORK_DEVICE_GROUP_6c38fb2e2dd45f4dab6ec3a19effd15a():
            self.network_device_group_create_network_device_group_response()
            return

        if self.matches_NETWORK_DEVICE_574ca6ab8ec556c3bc9531dc380b230a():
            self.network_device_create_network_device_response()
            return

        if self.matches_PORTAL_THEME_91eb833980f55025bfacbfcb8de814c8():
            self.portal_theme_create_portal_theme_response()
            return

        if self.matches_RADIUS_SERVER_SEQUENCE_83ad6ca0642c5750af6ca9905721a9d7():
            self.radius_server_sequence_create_radius_server_sequence_response()
            return

        if self.matches_RESTID_STORE_1073c23243c950f29b51f502c03d7058():
            self.restid_store_create_rest_id_store_response()
            return

        if self.matches_SECURITY_GROUPS_ACLS_9ab61f24bdaf508590f7686e1130913f():
            self.security_groups_acls_create_security_groups_acl_response()
            return

        if self.matches_SECURITY_GROUP_TO_VIRTUAL_NETWORK_97830a0710ba581da4d3fd00e84d59e3():
            self.security_group_to_virtual_network_create_security_groups_to_vn_to_vlan_response()
            return

        if self.matches_SECURITY_GROUPS_1d0290eb241f5bd79221afc8d6cb32da():
            self.security_groups_create_security_group_response()
            return

        if self.matches_SELF_REGISTERED_PORTAL_d524614e122d53d68324daf1681eb753():
            self.self_registered_portal_create_self_registered_portal_response()
            return

        if self.matches_SPONSOR_GROUP_56311acd30d35ee2ae16ff23757de7d8():
            self.sponsor_group_create_sponsor_group_response()
            return

        if self.matches_SPONSOR_PORTAL_1f15d19b858d59218ab56b7323ca2fae():
            self.sponsor_portal_create_sponsor_portal_response()
            return

        if self.matches_SPONSORED_GUEST_PORTAL_ca78559d8a9f559c87f53ea85169a2c7():
            self.sponsored_guest_portal_create_sponsored_guest_portal_response()
            return

        if self.matches_SXP_CONNECTIONS_789c371214c759f791c0a522b9eaf5b5():
            self.sxp_connections_create_sxp_connections_response()
            return

        if self.matches_SXP_LOCAL_BINDINGS_84610cf67e0155eab895b50d1a377f21():
            self.sxp_local_bindings_create_sxp_local_bindings_response()
            return

        if self.matches_SXP_VPNS_1a693347bdd15bb19d69a75f088498ce():
            self.sxp_vpns_create_sxp_vpn_response()
            return

        if self.matches_SYSTEM_CERTIFICATE_dd469dcee9445c72a3861ef94fb3b096():
            self.system_certificate_create_system_certificate_response()
            return

        if self.matches_TACACS_COMMAND_SETS_d9cc879878ee5a34ac1c32f2f0cb8c6d():
            self.tacacs_command_sets_create_tacacs_command_sets_response()
            return

        if self.matches_TACACS_EXTERNAL_SERVERS_b5097e4db7505ba390914b50b1c2046b():
            self.tacacs_external_servers_create_tacacs_external_servers_response()
            return

        if self.matches_TACACS_PROFILE_c094086382485201ad36d4641fc6822e():
            self.tacacs_profile_create_tacacs_profile_response()
            return

        if self.matches_TACACS_SERVER_SEQUENCE_5902a1e26e595667bd98f84dd29232e2():
            self.tacacs_server_sequence_create_tacacs_server_sequence_response()
            return

        if self.matches_CONSUMER_91101b93b991556cae0fdd562c5e3f63():
            self.consumer_create_account_response()
            return

        if self.matches_CONSUMER_d1f92a9024975e9dad6114255be546bd():
            self.consumer_activate_account_response()
            return

        if self.matches_CONSUMER_98c8ffe8c6095203a83131f49d4c8bb2():
            self.consumer_lookup_service_response()
            return

        if self.matches_CONSUMER_eaad68e7996c5562901de57bf5a0420a():
            self.consumer_access_secret_response()
            return

        if self.matches_MDM_3f66874f1141550da6104eff5428d37a():
            self.mdm_get_endpoints_response()
            return

        if self.matches_MDM_6419150c239256209b64afc9e5522e11():
            self.mdm_get_endpoint_by_mac_address_response()
            return

        if self.matches_MDM_0239282311e55709895e677699dfc3f7():
            self.mdm_get_endpoints_by_type_response()
            return

        if self.matches_MDM_339bf2a72bc05f5aabd3a79a5188d86a():
            self.mdm_get_endpoints_by_os_type_response()
            return

        if self.matches_PROFILER_dac693445cb95c6996cf6c7d85dece35():
            self.profiler_get_profiles_response()
            return

        if self.matches_PROVIDER_61c9daa26d4b5b80a41d4b7ff9359380():
            self.provider_register_service_response()
            return

        if self.matches_PROVIDER_b480aaa729e75e3d872d0b30a3f8b804():
            self.provider_unregister_service_response()
            return

        if self.matches_PROVIDER_ed4d852c55cd54c480986bec7fd9a8bb():
            self.provider_reregister_service_response()
            return

        if self.matches_PROVIDER_c9088df384b458c3991fed7f718971d5():
            self.provider_authorization_response()
            return

        if self.matches_SESSION_DIRECTORY_9a86b36d56165904911f133e10d4f955():
            self.session_directory_get_sessions_response()
            return

        if self.matches_SESSION_DIRECTORY_12d6da2024445b2cb8a146fe19889e71():
            self.session_directory_get_sessions_for_recovery_response()
            return

        if self.matches_SESSION_DIRECTORY_2515a470322e5500949321c2cbc1b9c9():
            self.session_directory_get_session_by_ip_address_response()
            return

        if self.matches_SESSION_DIRECTORY_e564f3d00647543db29d1ca6865bc8d0():
            self.session_directory_get_session_by_mac_address_response()
            return

        if self.matches_SESSION_DIRECTORY_f8021c1d176c5de9b8b41dcde0f0268e():
            self.session_directory_get_user_groups_response()
            return

        if self.matches_SESSION_DIRECTORY_1f674031faf65cac8e2f5581bdef4788():
            self.session_directory_get_user_group_by_user_name_response()
            return

        if self.matches_SYSTEM_HEALTH_0f67f5c0641d55708b20ffc56f374854():
            self.system_health_get_healths_response()
            return

        if self.matches_SYSTEM_HEALTH_048aadb0c21d5146a207994d493fe9a5():
            self.system_health_get_performances_response()
            return

        if self.matches_TRUST_SEC_CONFIGURATION_9b5b0eb1671a51758acf5ec364d80738():
            self.trust_sec_configuration_get_security_groups_response()
            return

        if self.matches_TRUST_SEC_CONFIGURATION_02b4aa5797455ee4a27390b77262992d():
            self.trust_sec_configuration_get_security_group_acls_response()
            return

        if self.matches_TRUST_SEC_CONFIGURATION_3da8b5be1a475510a5aa1593d625ffbb():
            self.trust_sec_configuration_get_egress_policies_response()
            return

        if self.matches_TRUST_SEC_CONFIGURATION_3f9e6e1c33155fdd9a88f48d093f375b():
            self.trust_sec_configuration_get_egress_matrices_response()
            return

        if self.matches_TRUST_SEC_SXP_900a7bddaf5159e68b2caeb19b9979c4():
            self.trust_sec_sxp_get_bindings_response()
            return

    def do_PUT(self):

        if self.matches_NODE_DEPLOYMENT_42b11e2f1af656bcb5880a7b33720ec5():
            self.node_deployment_promote_node_response()
            return

        if self.matches_NODE_DEPLOYMENT_682c1fa3bf115c77be99b602aca1493b():
            self.node_deployment_update_node_response()
            return

        if self.matches_NODE_GROUP_2875a99695fd5ee0b00efce79a5761ff():
            self.node_group_update_node_group_response()
            return

        if self.matches_BACKUP_AND_RESTORE_5329d31fa60f5575a2ed23cee473c0fc():
            self.backup_and_restore_update_scheduled_config_backup_response()
            return

        if self.matches_REPOSITORY_62488ad8eb56595e86c4300607ec4dd3():
            self.repository_update_repository_response()
            return

        if self.matches_ANC_ENDPOINT_2131fc6670fd50dfb04b1f6b16981256():
            self.anc_endpoint_clear_anc_endpoint_response()
            return

        if self.matches_ANC_ENDPOINT_136bc936bcb25464b9f3f227647b0443():
            self.anc_endpoint_apply_anc_endpoint_response()
            return

        if self.matches_ANC_ENDPOINT_5e6167fc5cb6593b8b48429187a26a67():
            self.anc_endpoint_bulk_request_for_anc_endpoint_response()
            return

        if self.matches_ANC_POLICY_1d79b507bda155c180d42f0a67ef64d5():
            self.anc_policy_update_anc_policy_by_id_response()
            return

        if self.matches_ANC_POLICY_4d67f9f6fba65dcbbcf64ca3e31b39a6():
            self.anc_policy_bulk_request_for_anc_policy_response()
            return

        if self.matches_CLEAR_THREATS_AND_VULNERABILITIES_e3110fc63ecb5428a075a8af8497fb35():
            self.clear_threats_and_vulnerabilities_clear_threats_and_vulnerabilities_response()
            return

        if self.matches_PX_GRID_NODE_a2a7f23f85105113954c87a917b7455f():
            self.px_grid_node_approve_px_grid_node_response()
            return

        if self.matches_SUPPORT_BUNDLE_DOWNLOAD_737531846d125b968b9d362a3458621d():
            self.support_bundle_download_download_support_bundle_response()
            return

        if self.matches_CERTIFICATES_e9594a91bd735eaabe2eb50038e9d05a():
            self.certificates_update_system_cert_response()
            return

        if self.matches_CERTIFICATES_ed4e0ba952525984acfe4a151689c2eb():
            self.certificates_update_trusted_certificate_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_7dc678d472905ab5bce9f4cba7cd7004():
            self.device_administration_authentication_rules_update_device_admin_policy_by_id_authentication_rule_by_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_e326f7a61069587f9a27e69433229cc7():
            self.device_administration_authorization_exception_rules_update_device_admin_policy_by_id_local_exception_rule_by_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_28042265da96552991705623287a164c():
            self.device_administration_authorization_global_exception_rules_put_device_admin_policy_set_global_exception_by_rule_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_80b60ed1eed75d7d9091344f4e38e2f1():
            self.device_administration_authorization_rules_update_device_admin_policy_by_id_authorization_rule_by_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_CONDITIONS_f0540adc16725e00adffdf57b67fb6ba():
            self.device_administration_conditions_put_device_admin_condition_by_condition_name_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_CONDITIONS_3b9b1bfd0f4151eb9812b474e4e4fa3c():
            self.device_administration_conditions_put_device_admin_condition_by_condition_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_b371441bddfd5d819a7aedfa215f4aeb():
            self.device_administration_network_conditions_put_device_admin_network_condition_by_condition_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_POLICY_SET_b6cc40e0f4b45e8da5908776d124ed5a():
            self.device_administration_policy_set_update_device_admin_policy_set_by_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_e3241242740252b2814e0b474c314e9b():
            self.device_administration_time_date_conditions_put_device_admin_time_condition_by_condition_id_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHENTICATION_RULES_ec5180b8603d5cf78c13d6d3c0be18c2():
            self.network_access_authentication_rules_update_network_access_policy_by_id_authentication_rule_by_id_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_d5c906da96395858b888f382e2ab9d79():
            self.network_access_authorization_exception_rules_update_network_access_policy_by_id_local_exception_rule_by_id_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_42639223458c51c99e8f35329c276126():
            self.network_access_authorization_global_exception_rules_update_network_access_policy_set_global_exception_rule_by_id_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_RULES_a8c6432bf3c8523e9876c4ac9d92c8b5():
            self.network_access_authorization_rules_update_network_access_policy_by_id_authorization_rule_by_id_response()
            return

        if self.matches_NETWORK_ACCESS_CONDITIONS_bbc720f738bf5b83a20de7e28e3c4c5f():
            self.network_access_conditions_put_network_access_condition_by_condition_name_response()
            return

        if self.matches_NETWORK_ACCESS_CONDITIONS_1f0d3cb73c4e59208d9ee04ffa787b3c():
            self.network_access_conditions_put_network_access_condition_by_condition_id_response()
            return

        if self.matches_NETWORK_ACCESS_DICTIONARY_e4f1e31aca1558f782a2cdb43853aaf2():
            self.network_access_dictionary_put_network_access_dictionaries_by_name_response()
            return

        if self.matches_NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_d2810d771d3e5ec580c39e0deb46b2b8():
            self.network_access_dictionary_attribute_put_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name_response()
            return

        if self.matches_NETWORK_ACCESS_NETWORK_CONDITIONS_5aaa481aaad35f8b8a7cbf2e063eac2b():
            self.network_access_network_conditions_put_network_access_network_condition_by_condition_id_response()
            return

        if self.matches_NETWORK_ACCESS_POLICY_SET_4068064fa27e5a779143ed557b417535():
            self.network_access_policy_set_update_network_access_policy_set_by_id_response()
            return

        if self.matches_NETWORK_ACCESS_TIME_DATE_CONDITIONS_fef057ddea8d56a98189b1db3bf5f240():
            self.network_access_time_date_conditions_put_network_access_time_condition_by_condition_id_response()
            return

        if self.matches_ACI_SETTINGS_1b155c91eec153338302d492db1afb80():
            self.aci_settings_test_aci_connectivity_response()
            return

        if self.matches_ACI_SETTINGS_56cea2e785ee57908a9ee3b118e49cfa():
            self.aci_settings_update_aci_settings_by_id_response()
            return

        if self.matches_ACTIVE_DIRECTORY_b839d4dee9b958e48ccef056603e253f():
            self.active_directory_get_all_user_groups_response()
            return

        if self.matches_ACTIVE_DIRECTORY_14104b05e80058df96e685baa727d578():
            self.active_directory_load_groups_from_domain_response()
            return

        if self.matches_ACTIVE_DIRECTORY_8091e84541805d1da1fa3d4d581102a9():
            self.active_directory_leave_domain_response()
            return

        if self.matches_ACTIVE_DIRECTORY_eae60ece5110590e97ddd910e8144ed2():
            self.active_directory_is_user_member_of_groups_response()
            return

        if self.matches_ACTIVE_DIRECTORY_7d0ed84901325292ad4e2a91a174f6b2():
            self.active_directory_get_all_trusted_domains_response()
            return

        if self.matches_ACTIVE_DIRECTORY_e84705b918955b53afe61fc37911eb8b():
            self.active_directory_join_domain_with_all_nodes_response()
            return

        if self.matches_ACTIVE_DIRECTORY_d011417d18d055ccb864c1dc2ae0456d():
            self.active_directory_leave_domain_with_all_nodes_response()
            return

        if self.matches_ACTIVE_DIRECTORY_48fd729f50e65695966359b589a1606b():
            self.active_directory_get_groups_by_domain_response()
            return

        if self.matches_ACTIVE_DIRECTORY_b3284240745e5b929c51495fe80bc1c4():
            self.active_directory_join_domain_response()
            return

        if self.matches_ALLOWED_PROTOCOLS_61a0b312f70257b1bfa90d0260f0c971():
            self.allowed_protocols_update_allowed_protocol_by_id_response()
            return

        if self.matches_AUTHORIZATION_PROFILE_9cb9f26e93655e7d89995b172f6fd97f():
            self.authorization_profile_update_authorization_profile_by_id_response()
            return

        if self.matches_BYOD_PORTAL_3e38d10b1ea257d49ebce893e87b3419():
            self.byod_portal_update_byod_portal_by_id_response()
            return

        if self.matches_CERTIFICATE_PROFILE_e09287aba99c56a6a9171b7e3a635a43():
            self.certificate_profile_update_certificate_profile_by_id_response()
            return

        if self.matches_DOWNLOADABLE_ACL_2d8c7ba0cb8f56d99135e16d2d973d11():
            self.downloadable_acl_update_downloadable_acl_by_id_response()
            return

        if self.matches_EGRESS_MATRIX_CELL_247716f503ab54e2921d713ed88f51c9():
            self.egress_matrix_cell_clear_all_matrix_cells_response()
            return

        if self.matches_EGRESS_MATRIX_CELL_90540642f47f525dbd71ef49710ef578():
            self.egress_matrix_cell_set_all_cells_status_response()
            return

        if self.matches_EGRESS_MATRIX_CELL_892a1e6c05d05e67906b3b59bbe6d274():
            self.egress_matrix_cell_clone_matrix_cell_response()
            return

        if self.matches_EGRESS_MATRIX_CELL_ce83fba942c25938bae0c7012df68317():
            self.egress_matrix_cell_update_egress_matrix_cell_by_id_response()
            return

        if self.matches_EGRESS_MATRIX_CELL_aa333658bf83576eb36a025283516518():
            self.egress_matrix_cell_bulk_request_for_egress_matrix_cell_response()
            return

        if self.matches_ENDPOINT_CERTIFICATE_8e27d5df9cbe5b29a7e16bb7c877a4ce():
            self.endpoint_certificate_create_endpoint_certificate_response()
            return

        if self.matches_ENDPOINT_IDENTITY_GROUP_189979b4e8d45639975c226dacd53e7b():
            self.endpoint_identity_group_update_endpoint_group_by_id_response()
            return

        if self.matches_ENDPOINT_258969f4f97557daacb3dadaced526cc():
            self.endpoint_release_rejected_endpoint_response()
            return

        if self.matches_ENDPOINT_ed121b2686e85bd5b28c068c3c0de220():
            self.endpoint_deregister_endpoint_response()
            return

        if self.matches_ENDPOINT_c8b30af4b84b5a90be2fc152cf26ad42():
            self.endpoint_update_endpoint_by_id_response()
            return

        if self.matches_ENDPOINT_dfaeea899c185169ae2a3b70b5491008():
            self.endpoint_register_endpoint_response()
            return

        if self.matches_ENDPOINT_c03505504e8e5af8a715e27c40f16eab():
            self.endpoint_bulk_request_for_endpoint_response()
            return

        if self.matches_EXTERNAL_RADIUS_SERVER_28036825e94f5eba9d9615a3ecc18ebc():
            self.external_radius_server_update_external_radius_server_by_id_response()
            return

        if self.matches_FILTER_POLICY_95d0006cc03d53c89a3593526bf8dc0f():
            self.filter_policy_update_filter_policy_by_id_response()
            return

        if self.matches_GUEST_SMTP_NOTIFICATION_CONFIGURATION_a7500f6e473a50e19452683e303dd021():
            self.guest_smtp_notification_configuration_update_guest_smtp_notification_settings_by_id_response()
            return

        if self.matches_GUEST_SSID_72e6e4b7d022556a80f1948efb3d5c61():
            self.guest_ssid_update_guest_ssid_by_id_response()
            return

        if self.matches_GUEST_TYPE_01c7aed7320e54bfac29f13c8717a6b5():
            self.guest_type_update_guest_type_email_response()
            return

        if self.matches_GUEST_TYPE_f9661f7c85c2570897cffc3d02668263():
            self.guest_type_update_guest_type_sms_response()
            return

        if self.matches_GUEST_TYPE_bac6d4d95ac45a0a8933b8712dcbe70d():
            self.guest_type_update_guest_type_by_id_response()
            return

        if self.matches_GUEST_USER_c67b4dcffba052ae8ece775bc61a1c21():
            self.guest_user_approve_guest_user_by_id_response()
            return

        if self.matches_GUEST_USER_2eb3472c4de150828b2dae61e2285313():
            self.guest_user_change_sponsor_password_response()
            return

        if self.matches_GUEST_USER_83983afcc8fe53b4824ae744a2ff3848():
            self.guest_user_suspend_guest_user_by_name_response()
            return

        if self.matches_GUEST_USER_18b21045846d5097a82cd61cb3c7eaf1():
            self.guest_user_reinstate_guest_user_by_name_response()
            return

        if self.matches_GUEST_USER_f24049df29d059c48eef86d381ffad5d():
            self.guest_user_update_guest_user_by_name_response()
            return

        if self.matches_GUEST_USER_7ea6ea4e41d85f83b6f6c10ce38bb9ed():
            self.guest_user_reset_guest_user_password_by_id_response()
            return

        if self.matches_GUEST_USER_4dfcba4a0f685c168bdf2b5b2be317ac():
            self.guest_user_reinstate_guest_user_by_id_response()
            return

        if self.matches_GUEST_USER_9a9fa9cbccbe50fcb1cd6a63fed47578():
            self.guest_user_update_guest_user_email_response()
            return

        if self.matches_GUEST_USER_290601ba14b751f98206ca2e19cff3fe():
            self.guest_user_update_guest_user_sms_response()
            return

        if self.matches_GUEST_USER_3c1e5e2a187652018c59b10155ac973d():
            self.guest_user_deny_guest_user_by_id_response()
            return

        if self.matches_GUEST_USER_8754551b9c7c5847b17684c49399ff95():
            self.guest_user_update_guest_user_by_id_response()
            return

        if self.matches_GUEST_USER_08be5b1e320e55f4a181370417471d9e():
            self.guest_user_suspend_guest_user_by_id_response()
            return

        if self.matches_GUEST_USER_37edfca30e8e514d9bab840c3c2d4c0f():
            self.guest_user_bulk_request_for_guest_user_response()
            return

        if self.matches_HOTSPOT_PORTAL_0ae4af25df565334b20a24c4878b68e4():
            self.hotspot_portal_update_hotspot_portal_by_id_response()
            return

        if self.matches_IDENTITY_GROUPS_1c0689e940ba5526946ad15976cc3365():
            self.identity_groups_update_identity_group_by_id_response()
            return

        if self.matches_IDENTITY_SEQUENCE_9c316d5e2fdd51bdab039ea9e2a417bd():
            self.identity_sequence_update_identity_sequence_by_id_response()
            return

        if self.matches_INTERNAL_USER_4758008519d9509db339e3b27dc56b37():
            self.internal_user_update_internal_user_by_name_response()
            return

        if self.matches_INTERNAL_USER_f7227b280b745b94bb801369b168a529():
            self.internal_user_update_internal_user_by_id_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_GROUP_bd7f3fb27d71596ebafecca578c85bc7():
            self.ip_to_sgt_mapping_group_deploy_ip_to_sgt_mapping_group_by_id_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_GROUP_0b8ef94d6d5554a4b57d37c52612ad7d():
            self.ip_to_sgt_mapping_group_deploy_all_ip_to_sgt_mapping_group_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_GROUP_d6c25690e3a854c5be7763a4106e379e():
            self.ip_to_sgt_mapping_group_get_deploy_status_ip_to_sgt_mapping_group_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_GROUP_02a5a26c964e53b3be3f9f0c103f304c():
            self.ip_to_sgt_mapping_group_update_ip_to_sgt_mapping_group_by_id_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_GROUP_a39fa17ffcd45736aa221dd27916e843():
            self.ip_to_sgt_mapping_group_bulk_request_for_ip_to_sgt_mapping_group_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_b5711af534e557749661afb5b6c90cee():
            self.ip_to_sgt_mapping_deploy_ip_to_sgt_mapping_by_id_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_83343989df7a50feb38d8729b99553e9():
            self.ip_to_sgt_mapping_deploy_all_ip_to_sgt_mapping_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_dcd55e1e57d25e65b625526a1d341afd():
            self.ip_to_sgt_mapping_get_deploy_status_ip_to_sgt_mapping_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_94de3cecd62e5153881245a8613fbeea():
            self.ip_to_sgt_mapping_update_ip_to_sgt_mapping_by_id_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_ab203a1dd0015924bf2005a84ae85477():
            self.ip_to_sgt_mapping_bulk_request_for_ip_to_sgt_mapping_response()
            return

        if self.matches_MY_DEVICE_PORTAL_83079c64b769537ea7c586565f6ed2a2():
            self.my_device_portal_update_my_device_portal_by_id_response()
            return

        if self.matches_NATIVE_SUPPLICANT_PROFILE_c54a2ad63f46527dbec140a05f1213b7():
            self.native_supplicant_profile_update_native_supplicant_profile_by_id_response()
            return

        if self.matches_NETWORK_DEVICE_GROUP_808461e6734850fabb2097fa969948cb():
            self.network_device_group_update_network_device_group_by_id_response()
            return

        if self.matches_NETWORK_DEVICE_2ea2c4586b845888b2a9375126f70de2():
            self.network_device_update_network_device_by_name_response()
            return

        if self.matches_NETWORK_DEVICE_b1edfeb182025176bb250633937177ae():
            self.network_device_update_network_device_by_id_response()
            return

        if self.matches_NETWORK_DEVICE_63b2eebd5c245e58a503aa53115eec53():
            self.network_device_bulk_request_for_network_device_response()
            return

        if self.matches_PORTAL_GLOBAL_SETTING_c97e7851003e5a63a2a8005ac8807dc7():
            self.portal_global_setting_update_portal_global_setting_by_id_response()
            return

        if self.matches_PORTAL_THEME_c82dcf6f2c3d5d399045050b02208db2():
            self.portal_theme_update_portal_theme_by_id_response()
            return

        if self.matches_PX_GRID_SETTINGS_787126e5dd9b5979a409b9f456265db0():
            self.px_grid_settings_autoapprove_px_grid_settings_response()
            return

        if self.matches_RADIUS_SERVER_SEQUENCE_df9ab8ff636353279d5c787585dcb6af():
            self.radius_server_sequence_update_radius_server_sequence_by_id_response()
            return

        if self.matches_RESTID_STORE_c85464a04f0e5ddc99f8e6b8ed0f7eac():
            self.restid_store_update_rest_id_store_by_name_response()
            return

        if self.matches_RESTID_STORE_ded7f8573c255c318bb1f04bfdbf01e1():
            self.restid_store_update_rest_id_store_by_id_response()
            return

        if self.matches_SECURITY_GROUPS_ACLS_afc81cd1e25c50319f75606b97c23b3d():
            self.security_groups_acls_update_security_groups_acl_by_id_response()
            return

        if self.matches_SECURITY_GROUPS_ACLS_bfff136597e25df5ae1d135251fee263():
            self.security_groups_acls_bulk_request_for_security_groups_acl_response()
            return

        if self.matches_SECURITY_GROUP_TO_VIRTUAL_NETWORK_eae98db0c24b5ecca77cce8279e20785():
            self.security_group_to_virtual_network_update_security_groups_to_vn_to_vlan_by_id_response()
            return

        if self.matches_SECURITY_GROUP_TO_VIRTUAL_NETWORK_0ff196187ee45a92bf195593ab8f102e():
            self.security_group_to_virtual_network_bulk_request_for_security_groups_to_vn_to_vlan_response()
            return

        if self.matches_SECURITY_GROUPS_42ce666e64a958229cfd8da70945935e():
            self.security_groups_update_security_group_by_id_response()
            return

        if self.matches_SECURITY_GROUPS_fe0ac7fc07885c6f877768654aefd189():
            self.security_groups_bulk_request_for_security_group_response()
            return

        if self.matches_SELF_REGISTERED_PORTAL_400c4fada6c558d9aba09cc373d5b266():
            self.self_registered_portal_update_self_registered_portal_by_id_response()
            return

        if self.matches_SPONSOR_GROUP_dfc44f7f24d153d789efa48e904b3832():
            self.sponsor_group_update_sponsor_group_by_id_response()
            return

        if self.matches_SPONSOR_PORTAL_bd8691c5d9435e48a3c7a08658bda585():
            self.sponsor_portal_update_sponsor_portal_by_id_response()
            return

        if self.matches_SPONSORED_GUEST_PORTAL_0d39172f68fd5cbd897f03f1440f98a4():
            self.sponsored_guest_portal_update_sponsored_guest_portal_by_id_response()
            return

        if self.matches_SXP_CONNECTIONS_1cab8440e21553c3a807d23d05e5e1aa():
            self.sxp_connections_update_sxp_connections_by_id_response()
            return

        if self.matches_SXP_CONNECTIONS_a9d9ce4538605d439015d3ed7ef88c41():
            self.sxp_connections_bulk_request_for_sxp_connections_response()
            return

        if self.matches_SXP_LOCAL_BINDINGS_313e07cb8ea65820863cce345c67926b():
            self.sxp_local_bindings_update_sxp_local_bindings_by_id_response()
            return

        if self.matches_SXP_LOCAL_BINDINGS_2b97435f47305f5da136a0d68ac6d466():
            self.sxp_local_bindings_bulk_request_for_sxp_local_bindings_response()
            return

        if self.matches_SXP_VPNS_be45eed0938a5143bf85ffd5fd4205d0():
            self.sxp_vpns_bulk_request_for_sxp_vpns_response()
            return

        if self.matches_TACACS_COMMAND_SETS_20eb6323be425816a4116eea48f16f4b():
            self.tacacs_command_sets_update_tacacs_command_sets_by_id_response()
            return

        if self.matches_TACACS_EXTERNAL_SERVERS_7a7cffe3bfae55aa81b7b4447519e4cd():
            self.tacacs_external_servers_update_tacacs_external_servers_by_id_response()
            return

        if self.matches_TACACS_PROFILE_4a0db9ec45c05879a6f016a1edf54793():
            self.tacacs_profile_update_tacacs_profile_by_id_response()
            return

        if self.matches_TACACS_SERVER_SEQUENCE_7a7cffe3bfae55aa81b7b4447519e4cd():
            self.tacacs_server_sequence_update_tacacs_server_sequence_by_id_response()
            return

    def do_DELETE(self):

        if self.matches_NODE_DEPLOYMENT_161d26670a205a78800cb50673027a6e():
            self.node_deployment_delete_node_response()
            return

        if self.matches_NODE_GROUP_2c5c37c343c050e0af67b2223e64faf3():
            self.node_group_delete_node_group_response()
            return

        if self.matches_PAN_HA_a1e3cde0c3f254b39caaaf7c907ae67e():
            self.pan_ha_disable_pan_ha_response()
            return

        if self.matches_REPOSITORY_d3b49f09d7f954bdb6f413e1785a05d7():
            self.repository_delete_repository_response()
            return

        if self.matches_ANC_POLICY_7c6b8dd764e052699d4d7a0d8ba43640():
            self.anc_policy_delete_anc_policy_by_id_response()
            return

        if self.matches_PX_GRID_NODE_849e718d5054593b94a2fef39461c24a():
            self.px_grid_node_delete_px_grid_node_by_name_response()
            return

        if self.matches_CERTIFICATES_dde06bf20b6b5f71b8f0782f3750c242():
            self.certificates_delete_csr_response()
            return

        if self.matches_CERTIFICATES_5c55df3640a55c48bece27159ce199f8():
            self.certificates_delete_system_certificate_by_id_response()
            return

        if self.matches_CERTIFICATES_de9ebc73cfce5059a702076cf6a0aec2():
            self.certificates_delete_trusted_certificate_by_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHENTICATION_RULES_a0a005e87c6755e0bf5d4454a98f08c5():
            self.device_administration_authentication_rules_delete_device_admin_policy_by_id_authentication_rule_by_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_EXCEPTION_RULES_7c12c4eb2a5650c2b6e26a84131ef65b():
            self.device_administration_authorization_exception_rules_delete_device_admin_policy_by_id_local_exception_rule_by_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_10281a20040d51a1ba61f4d210195e59():
            self.device_administration_authorization_global_exception_rules_delete_device_admin_policyset_global_exception_by_rule_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_AUTHORIZATION_RULES_e7979abd11155f12b1336bbf02a99687():
            self.device_administration_authorization_rules_delete_device_admin_policy_by_id_authorization_rule_by_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_CONDITIONS_c276cf1dc9545d45ae3f871966cb664b():
            self.device_administration_conditions_delete_device_admin_condition_by_condition_name_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_CONDITIONS_2a6c1759c65b51a09ed7981397ece5c6():
            self.device_administration_conditions_delete_device_admin_condition_by_condition_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_NETWORK_CONDITIONS_037e7b011df45066b55be86033ecd17a():
            self.device_administration_network_conditions_delete_device_admin_network_condition_by_condition_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_POLICY_SET_f602e2f88378502a8d8bca6dff274afe():
            self.device_administration_policy_set_delete_device_admin_policy_set_by_id_response()
            return

        if self.matches_DEVICE_ADMINISTRATION_TIME_DATE_CONDITIONS_cf9f01129179555aa60c446f0a65c65a():
            self.device_administration_time_date_conditions_delete_device_admin_time_condition_by_condition_id_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHENTICATION_RULES_da4f3b797ace547fa8f298d8c5197ce8():
            self.network_access_authentication_rules_delete_network_access_policy_by_id_authentication_rule_by_id_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_EXCEPTION_RULES_0d60e4de79065869a39a937f02e3e885():
            self.network_access_authorization_exception_rules_delete_network_access_policy_by_id_local_exception_rule_by_id_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_GLOBAL_EXCEPTION_RULES_61e00af18a485a9283811feb84b04843():
            self.network_access_authorization_global_exception_rules_delete_network_access_policy_set_global_exception_rule_by_id_response()
            return

        if self.matches_NETWORK_ACCESS_AUTHORIZATION_RULES_0f8c47fa229d5f749f7432510709876c():
            self.network_access_authorization_rules_delete_network_access_policy_by_id_authorization_rule_by_id_response()
            return

        if self.matches_NETWORK_ACCESS_CONDITIONS_1ccbc1ec86665500b4520ba48304eab7():
            self.network_access_conditions_delete_network_access_condition_by_condition_name_response()
            return

        if self.matches_NETWORK_ACCESS_CONDITIONS_010c97b4161c5b95a6a83b6917ce26d6():
            self.network_access_conditions_delete_network_access_condition_by_condition_id_response()
            return

        if self.matches_NETWORK_ACCESS_DICTIONARY_2b80087f14af51d186a7bfa89f5a494b():
            self.network_access_dictionary_delete_network_access_dictionaries_by_name_response()
            return

        if self.matches_NETWORK_ACCESS_DICTIONARY_ATTRIBUTE_e1725efd8ea253d1930913a85709977f():
            self.network_access_dictionary_attribute_delete_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name_response()
            return

        if self.matches_NETWORK_ACCESS_NETWORK_CONDITIONS_8e345ca7adb75b1bacfa42771a4d242c():
            self.network_access_network_conditions_delete_network_access_network_condition_by_condition_id_response()
            return

        if self.matches_NETWORK_ACCESS_POLICY_SET_c1d0c2c01a5856fa8be5af8e2b07e420():
            self.network_access_policy_set_delete_network_access_policy_set_by_id_response()
            return

        if self.matches_NETWORK_ACCESS_TIME_DATE_CONDITIONS_10517292296559f2847ac681d93cf40b():
            self.network_access_time_date_conditions_delete_network_access_time_condition_by_condition_id_response()
            return

        if self.matches_ACTIVE_DIRECTORY_786febbe79ed5bb780d97a98f292b606():
            self.active_directory_delete_active_directory_by_id_response()
            return

        if self.matches_ALLOWED_PROTOCOLS_a6cbd2c420785cfcbdecc3495bca8af4():
            self.allowed_protocols_delete_allowed_protocol_by_id_response()
            return

        if self.matches_AUTHORIZATION_PROFILE_c3913dfbda305f678ede16f782762ad3():
            self.authorization_profile_delete_authorization_profile_by_id_response()
            return

        if self.matches_BYOD_PORTAL_df2fb34fbab65254ac87d1be50abd15f():
            self.byod_portal_delete_byod_portal_by_id_response()
            return

        if self.matches_DOWNLOADABLE_ACL_42b3db444eaa50678218c29f88de60e8():
            self.downloadable_acl_delete_downloadable_acl_by_id_response()
            return

        if self.matches_EGRESS_MATRIX_CELL_e4393915121d5bcc94dfde6c8f6f7f1c():
            self.egress_matrix_cell_delete_egress_matrix_cell_by_id_response()
            return

        if self.matches_ENDPOINT_IDENTITY_GROUP_f7b0aab2a65652feae637779bfb20d2d():
            self.endpoint_identity_group_delete_endpoint_group_by_id_response()
            return

        if self.matches_ENDPOINT_36658f1cac5f578ab6509196266ad8e3():
            self.endpoint_delete_endpoint_by_id_response()
            return

        if self.matches_EXTERNAL_RADIUS_SERVER_373fcbde1c215f95bebbfa95780ed9a8():
            self.external_radius_server_delete_external_radius_server_by_id_response()
            return

        if self.matches_FILTER_POLICY_4a83e0d4f56a5c06946f685aa46fa3e3():
            self.filter_policy_delete_filter_policy_by_id_response()
            return

        if self.matches_GUEST_SSID_8328407df7345f788230a512d6635c25():
            self.guest_ssid_delete_guest_ssid_by_id_response()
            return

        if self.matches_GUEST_TYPE_6faa7211d68e5b329034e17c82b78694():
            self.guest_type_delete_guest_type_by_id_response()
            return

        if self.matches_GUEST_USER_76ef15d7c6b259f5859ee9675c38887c():
            self.guest_user_delete_guest_user_by_name_response()
            return

        if self.matches_GUEST_USER_1030e251b39f55d3ac2570a963a3ee9c():
            self.guest_user_delete_guest_user_by_id_response()
            return

        if self.matches_HOTSPOT_PORTAL_1a344d1c6f535789b7badbaa502e8d3b():
            self.hotspot_portal_delete_hotspot_portal_by_id_response()
            return

        if self.matches_IDENTITY_SEQUENCE_2b8258803668534d87781e995c73c23a():
            self.identity_sequence_delete_identity_sequence_by_id_response()
            return

        if self.matches_INTERNAL_USER_2447b4e2fc3e595aa1be86d6589614b9():
            self.internal_user_delete_internal_user_by_name_response()
            return

        if self.matches_INTERNAL_USER_dcf28db5184e51139b15f9ffccd10b67():
            self.internal_user_delete_internal_user_by_id_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_GROUP_73ebc15160cf5c0184d3eaff3be14508():
            self.ip_to_sgt_mapping_group_delete_ip_to_sgt_mapping_group_by_id_response()
            return

        if self.matches_IP_TO_SGT_MAPPING_582650f0cb1e55c9baee89c136c8ec47():
            self.ip_to_sgt_mapping_delete_ip_to_sgt_mapping_by_id_response()
            return

        if self.matches_MY_DEVICE_PORTAL_c04f18d6afee5f649a5700bf3074adb9():
            self.my_device_portal_delete_my_device_portal_by_id_response()
            return

        if self.matches_NATIVE_SUPPLICANT_PROFILE_3fff9d421c78597d98a54dd08a9a99f9():
            self.native_supplicant_profile_delete_native_supplicant_profile_by_id_response()
            return

        if self.matches_NETWORK_DEVICE_GROUP_9291975ded6653128f502c97e52cf279():
            self.network_device_group_delete_network_device_group_by_id_response()
            return

        if self.matches_NETWORK_DEVICE_116eafaf2e785c6898fb982dbe4462e7():
            self.network_device_delete_network_device_by_name_response()
            return

        if self.matches_NETWORK_DEVICE_9f2fd3c6324b581ca0f3f9eadede1cdc():
            self.network_device_delete_network_device_by_id_response()
            return

        if self.matches_PORTAL_THEME_8567c39e537955888cc23e4f90e6449b():
            self.portal_theme_delete_portal_theme_by_id_response()
            return

        if self.matches_RADIUS_SERVER_SEQUENCE_815b13838fa75d6e8d970f6eeb6a4510():
            self.radius_server_sequence_delete_radius_server_sequence_by_id_response()
            return

        if self.matches_RESTID_STORE_e068a8dc1ed65f8d9cdfa70a49f543e0():
            self.restid_store_delete_rest_id_store_by_name_response()
            return

        if self.matches_RESTID_STORE_2e77a1dd4aa75dcebbc3ee4e94a162b4():
            self.restid_store_delete_rest_id_store_by_id_response()
            return

        if self.matches_SECURITY_GROUPS_ACLS_b0a2bea8bfec52b68663ef3f7ac6d7a7():
            self.security_groups_acls_delete_security_groups_acl_by_id_response()
            return

        if self.matches_SECURITY_GROUP_TO_VIRTUAL_NETWORK_9462680497c852dbb953860bef3326e0():
            self.security_group_to_virtual_network_delete_security_groups_to_vn_to_vlan_by_id_response()
            return

        if self.matches_SECURITY_GROUPS_ed2c0f81f4ea5299840089761bfd4f62():
            self.security_groups_delete_security_group_by_id_response()
            return

        if self.matches_SELF_REGISTERED_PORTAL_673f9ada2e275fa2934fdb4825266a2c():
            self.self_registered_portal_delete_self_registered_portal_by_id_response()
            return

        if self.matches_SPONSOR_GROUP_61c28a45acf05fec98879d8d2ac51129():
            self.sponsor_group_delete_sponsor_group_by_id_response()
            return

        if self.matches_SPONSOR_PORTAL_d8d4c7451f7f5e2faae4e8ac530b5f08():
            self.sponsor_portal_delete_sponsor_portal_by_id_response()
            return

        if self.matches_SPONSORED_GUEST_PORTAL_9218749931f05e2ebc796f080892085f():
            self.sponsored_guest_portal_delete_sponsored_guest_portal_by_id_response()
            return

        if self.matches_SXP_CONNECTIONS_65954377fb665776b98ba815b52515a6():
            self.sxp_connections_delete_sxp_connections_by_id_response()
            return

        if self.matches_SXP_LOCAL_BINDINGS_77db04edfe595fbba5b49eb71dcb65bd():
            self.sxp_local_bindings_delete_sxp_local_bindings_by_id_response()
            return

        if self.matches_SXP_VPNS_8a0501930cc9517ea1cb4103db6e0af7():
            self.sxp_vpns_delete_sxp_vpn_by_id_response()
            return

        if self.matches_TACACS_COMMAND_SETS_4a319a83b14252eba0f00bb4c4ab0d7c():
            self.tacacs_command_sets_delete_tacacs_command_sets_by_id_response()
            return

        if self.matches_TACACS_EXTERNAL_SERVERS_896816622564523798353b885b115048():
            self.tacacs_external_servers_delete_tacacs_external_servers_by_id_response()
            return

        if self.matches_TACACS_PROFILE_9fd38182c505549fbc0d8c1122c1f685():
            self.tacacs_profile_delete_tacacs_profile_by_id_response()
            return

        if self.matches_TACACS_SERVER_SEQUENCE_896816622564523798353b885b115048():
            self.tacacs_server_sequence_delete_tacacs_server_sequence_by_id_response()
            return

        if self.matches_MISC_549bd2a2c3735c6ca7b59c86d428e222():
            self.misc_delete_all_sessions_response()
            return
