# -*- coding: utf-8 -*-

import re

def uni2zg(value):
	rule = [
	    {
	        "from": ur"\u1004\u103a\u1039",
	        "to": ur"\u1064"
	    },
	    {
	        "from": ur"\u1039\u1010\u103d",
	        "to": ur"\u1096"
	    },
	    {
	        "from": ur"\u102b\u103a",
	        "to": ur"\u105a"
	    },
	    {
	        "from": ur"\u100b\u1039\u100c",
	        "to": ur"\u1092"
	    },
	    {
	        "from": ur"\u102d\u1036",
	        "to": ur"\u108e"
	    },
	    {
	        "from": ur"\u104e\u1004\u103a\u1038",
	        "to": ur"\u104e"
	    },
	    {
	        "from": ur"[\u1025\u1009](?=[\u1039\u102f\u1030])",
	        "to": ur"\u106a"
	    },
	    {
	        "from": ur"[\u1025\u1009](?=[\u1037]?[\u103a])",
	        "to": ur"\u1025"
	    },
	    {
	        "from": ur"\u100a(?=[\u1039\u103d])",
	        "to": ur"\u106b"
	    },
	    {
	        "from": ur"(\u1039[\u1000-\u1021])(\u102D){0,1}\u102f",
	        "to": ur"\1\2\u1033"
	    },
	    {
	        "from": ur"(\u1039[\u1000-\u1021])\u1030",
	        "to": ur"\1\u1034"
	    },
	    {
	        "from": ur"\u1014(?=[\u102d\u102e\u102f\u103A]?[\u1030\u103d\u103e\u102f\u1039])",
	        "to": ur"\u108f"
	    },
	    {
	        "from": ur"\u1014(?=\u103A\u102F )",
	        "to": ur"\u108f"
	    },
	    {
	        "from" : ur"\u1014\u103c",
	        "to" : ur"\u108f\u103c"
	    },
	    {
	        "from": ur"\u1039\u1000",
	        "to": ur"\u1060"
	    },
	    {
	        "from": ur"\u1039\u1001",
	        "to": ur"\u1061"
	    },
	    {
	        "from": ur"\u1039\u1002",
	        "to": ur"\u1062"
	    },
	    {
	        "from": ur"\u1039\u1003",
	        "to": ur"\u1063"
	    },
	    {
	        "from": ur"\u1039\u1005",
	        "to": ur"\u1065"
	    },
	    {
	        "from": ur"\u1039\u1006",
	        "to": ur"\u1066"
	    },
	    {
	        "from": ur"\u1039\u1007",
	        "to": ur"\u1068"
	    },
	    {
	        "from": ur"\u1039\u1008",
	        "to": ur"\u1069"
	    },
	    {
	        "from": ur"\u1039\u100b",
	        "to": ur"\u106c"
	    },
	    {
	        "from": ur"\u1039\u100c",
	        "to": ur"\u106d"
	    },
	    {
	        "from": ur"\u100d\u1039\u100d",
	        "to": ur"\u106e"
	    },
	    {
	        "from": ur"\u100d\u1039\u100e",
	        "to": ur"\u106f"
	    },
	    {
	        "from": ur"\u1039\u100f",
	        "to": ur"\u1070"
	    },
	    {
	        "from": ur"\u1039\u1010",
	        "to": ur"\u1071"
	    },
	    {
	        "from": ur"\u1039\u1011",
	        "to": ur"\u1073"
	    },
	    {
	        "from": ur"\u1039\u1012",
	        "to": ur"\u1075"
	    },
	    {
	        "from": ur"\u1039\u1013",
	        "to": ur"\u1076"
	    },
	    {
	        "from": ur"\u1039[\u1014\u108f]",
	        "to": ur"\u1077"
	    },
	    {
	        "from": ur"\u1039\u1015",
	        "to": ur"\u1078"
	    },
	    {
	        "from": ur"\u1039\u1016",
	        "to": ur"\u1079"
	    },
	    {
	        "from": ur"\u1039\u1017",
	        "to": ur"\u107a"
	    },
	    {
	        "from": ur"\u1039\u1018",
	        "to": ur"\u107b"
	    },
	    {
	        "from": ur"\u1039\u1019",
	        "to": ur"\u107c"
	    },
	    {
	        "from": ur"\u1039\u101c",
	        "to": ur"\u1085"
	    },
	    {
	        "from": ur"\u103f",
	        "to": ur"\u1086"
	    },
	    {
	        "from": ur"\u103d\u103e",
	        "to": ur"\u108a"
	    },
	    {
	        "from": ur"(\u1064)([\u1000-\u1021])([\u103b\u103c]?)\u102d",
	        "to": ur"\2\3\u108b"
	    },
	    {
	        "from": ur"(\u1064)([\u1000-\u1021])([\u103b\u103c]?)\u102e",
	        "to": ur"\2\3\u108c"
	    },
	    {
	        "from": ur"(\u1064)([\u1000-\u1021])([\u103b\u103c]?)\u1036",
	        "to": ur"\2\3\u108d"
	    },
	    {
	        "from": ur"(\u1064)([\u1000-\u1021])([\u103b\u103c]?)([\u1031]?)",
	        "to": ur"\2\3\4\1"
	    },
	    {
	        "from": ur"\u101b(?=([\u102d\u102e]?)[\u102f\u1030\u103d\u108a])",
	        "to": ur"\u1090"
	    },
	    {
	        "from": ur"\u100f\u1039\u100d",
	        "to": ur"\u1091"
	    },
	    {
	        "from": ur"\u100b\u1039\u100b",
	        "to": ur"\u1097"
	    },
	    {
	        "from": ur"([\u1000-\u1021\u108f\u1029\u106e\u106f\u1086\u1090\u1091\u1092\u1097])([\u1060-\u1069\u106c\u106d\u1070-\u107c\u1085\u108a])?([\u103b-\u103e]*)?\u1031",
	        "to": ur"\u1031\1\2\3"
	    },
	    {
	        "from": ur"\u103c\u103e",
	        "to": ur"\u103c\u1087"
	    },
	    {
	        "from": ur"([\u1000-\u1021\u108f\u1029])([\u1060-\u1069\u106c\u106d\u1070-\u107c\u1085])?(\u103c)",
	        "to": ur"\3\1\2"
	    },
	    {
	        "from": ur"\u103a",
	        "to": ur"\u1039"
	    },
	    {
	        "from": ur"\u103b",
	        "to": ur"\u103a"
	    },
	    {
	        "from": ur"\u103c",
	        "to": ur"\u103b"
	    },
	    {
	        "from": ur"\u103d",
	        "to": ur"\u103c"
	    },
	    {
	        "from": ur"\u103e",
	        "to": ur"\u103d"
	    },
	    {
	        "from": ur"([^\u103a\u100a])\u103d([\u102d\u102e]?)\u102f",
	        "to": ur"\1\u1088\2"
	    },
	    {
	        "from": ur"([\u101b\u103a\u103c\u108a\u1088\u1090])([\u1030\u103d])?([\u1032\u1036\u1039\u102d\u102e\u108b\u108c\u108d\u108e]?)(\u102f)?\u1037",
	        "to": ur"\1\2\3\4\u1095"
	    },
	    {
	        "from": ur"([\u102f\u1014\u1030\u103d])([\u1032\u1036\u1039\u102d\u102e\u108b\u108c\u108d\u108e]?)\u1037",
	        "to": ur"\1\2\u1094"
	    },
	    {
	        "from": ur"([\u103b])([\u1000-\u1021])([\u1087]?)([\u1036\u102d\u102e\u108b\u108c\u108d\u108e]?)\u102f",
	        "to": ur"\1\2\3\4\u1033"
	    },
	    {
	        "from": ur"([\u103b])([\u1000-\u1021])([\u1087]?)([\u1036\u102d\u102e\u108b\u108c\u108d\u108e]?)\u1030",
	        "to": ur"\1\2\3\4\u1034"
	    },
	    {
	        "from": ur"([\u103a\u103c\u100a\u1020\u1025])([\u103d]?)([\u1036\u102d\u102e\u108b\u108c\u108d\u108e]?)\u102f",
	        "to": ur"\1\2\3\u1033"
	    },
	    {
	        "from": ur"([\u103a\u103c\u100a\u101b])(\u103d?)([\u1036\u102d\u102e\u108b\u108c\u108d\u108e]?)\u1030",
	        "to": ur"\1\2\3\u1034"
	    },
	    {
	        "from": ur"\u100a\u103d",
	        "to": ur"\u100a\u1087"
	    },
	    {
	        "from": ur"\u103d\u1030",
	        "to": ur"\u1089"
	    },
	    {
	        "from": ur"\u103b([\u1000\u1003\u1006\u100f\u1010\u1011\u1018\u101a\u101c\u101a\u101e\u101f])",
	        "to": ur"\u107e\1"
	    },
	    {
	        "from": ur"\u107e([\u1000\u1003\u1006\u100f\u1010\u1011\u1018\u101a\u101c\u101a\u101e\u101f])([\u103c\u108a])([\u1032\u1036\u102d\u102e\u108b\u108c\u108d\u108e])",
	        "to": ur"\u1084\1\2\3"
	    },
	    {
	        "from": ur"\u107e([\u1000\u1003\u1006\u100f\u1010\u1011\u1018\u101a\u101c\u101a\u101e\u101f])([\u103c\u108a])",
	        "to": ur"\u1082\1\2"
	    },
	    {
	        "from": ur"\u107e([\u1000\u1003\u1006\u100f\u1010\u1011\u1018\u101a\u101c\u101a\u101e\u101f])([\u1033\u1034]?)([\u1032\u1036\u102d\u102e\u108b\u108c\u108d\u108e])",
	        "to": ur"\u1080\1\2\3"
	    },
	    {
	        "from": ur"\u103b([\u1000-\u1021])([\u103c\u108a])([\u1032\u1036\u102d\u102e\u108b\u108c\u108d\u108e])",
	        "to": ur"\u1083\1\2\3"
	    },
	    {
	        "from": ur"\u103b([\u1000-\u1021])([\u103c\u108a])",
	        "to": ur"\u1081\1\2"
	    },
	    {
	        "from": ur"\u103b([\u1000-\u1021])([\u1033\u1034]?)([\u1032\u1036\u102d\u102e\u108b\u108c\u108d\u108e])",
	        "to": ur"\u107f\1\2\3"
	    },
	    {
	        "from": ur"\u103a\u103d",
	        "to": ur"\u103d\u103a"
	    },
	    {
	        "from": ur"\u103a([\u103c\u108a])",
	        "to": ur"\1\u107d"
	    },
	    {
	        "from": ur"([\u1033\u1034])\u1094",
	        "to": ur"\1\u1095"
	    },
	    {
	      "from": ur"\u108F\u1071",
	      "to" : ur"\u108F\u1072"
	    },
	    {
	      "from": ur"([\u1000-\u1021])([\u107B\u1066])\u102C",
	      "to": ur"\1\u102C\2"
	    },
	    {
	      "from": ur"\u102C([\u107B\u1066])\u1037",
	      "to": ur"\u102C\1\u1094"
	    }
	]
	return replace_with_rule(rule, value)

def zg2uni(value):
	rule = [
	    {
	        "from" : ur"([\u102D\u102E\u103D\u102F\u1037\u1095])\\1+",
	        "to": ur"\1"
	    },
	    {
	        "from": ur"\u200B",
	        "to": ur""
	    },
	    {
	        "from" : ur"\u103d\u103c",
	        "to" : ur"\u108a"
	    },
	    {
	        "from": ur"(\u103d|\u1087)",
	        "to": ur"\u103e"
	    },
	    {
	        "from": ur"\u103c",
	        "to": ur"\u103d"
	    },
	    {
	        "from": ur"(\u103b|\u107e|\u107f|\u1080|\u1081|\u1082|\u1083|\u1084)",
	        "to": ur"\u103c"
	    },
	    {
	        "from": ur"(\u103a|\u107d)",
	        "to": ur"\u103b"
	    },
	    {
	        "from": ur"\u1039",
	        "to": ur"\u103a"
	    },
	    {
	        "from": ur"(\u1066|\u1067)",
	        "to": ur"\u1039\u1006"
	    },
	    {
	        "from": ur"\u106a",
	        "to": ur"\u1009"
	    },
	    {
	        "from": ur"\u106b",
	        "to": ur"\u100a"
	    },
	    {
	        "from": ur"\u106c",
	        "to": ur"\u1039\u100b"
	    },
	    {
	        "from": ur"\u106d",
	        "to": ur"\u1039\u100c"
	    },
	    {
	        "from": ur"\u106e",
	        "to": ur"\u100d\u1039\u100d"
	    },
	    {
	        "from": ur"\u106f",
	        "to": ur"\u100d\u1039\u100e"
	    },
	    {
	        "from": ur"\u1070",
	        "to": ur"\u1039\u100f"
	    },
	    {
	        "from": ur"(\u1071|\u1072)",
	        "to": ur"\u1039\u1010"
	    },
	    {
	        "from": ur"\u1060",
	        "to": ur"\u1039\u1000"
	    },
	    {
	        "from": ur"\u1061",
	        "to": ur"\u1039\u1001"
	    },
	    {
	        "from": ur"\u1062",
	        "to": ur"\u1039\u1002"
	    },
	    {
	        "from": ur"\u1063",
	        "to": ur"\u1039\u1003"
	    },
	    {
	        "from": ur"\u1065",
	        "to": ur"\u1039\u1005"
	    },
	    {
	        "from": ur"\u1068",
	        "to": ur"\u1039\u1007"
	    },
	    {
	        "from": ur"\u1069",
	        "to": ur"\u1039\u1008"
	    },
	    {
	        "from": ur"(\u1073|\u1074)",
	        "to": ur"\u1039\u1011"
	    },
	    {
	        "from": ur"\u1075",
	        "to": ur"\u1039\u1012"
	    },
	    {
	        "from": ur"\u1076",
	        "to": ur"\u1039\u1013"
	    },
	    {
	        "from": ur"\u1077",
	        "to": ur"\u1039\u1014"
	    },
	    {
	        "from": ur"\u1078",
	        "to": ur"\u1039\u1015"
	    },
	    {
	        "from": ur"\u1079",
	        "to": ur"\u1039\u1016"
	    },
	    {
	        "from": ur"\u107a",
	        "to": ur"\u1039\u1017"
	    },
	    {
	        "from": ur"\u107c",
	        "to": ur"\u1039\u1019"
	    },
	    {
	        "from": ur"\u1085",
	        "to": ur"\u1039\u101c"
	    },
	    {
	        "from": ur"\u1033",
	        "to": ur"\u102f"
	    },
	    {
	        "from": ur"\u1034",
	        "to": ur"\u1030"
	    },
	    {
	        "from": ur"\u103f",
	        "to": ur"\u1030"
	    },
	    {
	        "from": ur"\u1086",
	        "to": ur"\u103f"
	    },
	    {
	        "from": ur"\u1036\u1088",
	        "to": ur"\u1088\u1036"
	    },
	    {
	        "from": ur"\u1088",
	        "to": ur"\u103e\u102f"
	    },
	    {
	        "from": ur"\u1089",
	        "to": ur"\u103e\u1030"
	    },
	    {
	        "from": ur"\u108a",
	        "to": ur"\u103d\u103e"
	    },
	    {
	        "from": ur"\u103B\u1064",
	        "to": ur"\u1064\u103B"
	    },
	    {
	        "from": ur"(\u1031)?([\u1000-\u1021])\u1064",
	        "to": ur"\u1004\u103a\u1039\1\2"
	    },
	    {
	        "from": ur"(\u1031)?([\u1000-\u1021])(\u103b)?\u108b",
	        "to": ur"\u1004\u103a\u1039\1\2\3\u102d"
	    },
	    {
	        "from": ur"(\u1031)?([\u1000-\u1021])(\u103b)?\u108c",
	        "to": ur"\u1004\u103a\u1039\1\2\3\u102e"
	    },
	    {
	        "from": ur"(\u1031)?([\u1000-\u1021])\u108d",
	        "to": ur"\u1004\u103a\u1039\1\2\u1036"
	    },
	    {
	        "from": ur"\u108e",
	        "to": ur"\u102d\u1036"
	    },
	    {
	        "from": ur"\u108f",
	        "to": ur"\u1014"
	    },
	    {
	        "from": ur"\u1090",
	        "to": ur"\u101b"
	    },
	    {
	        "from": ur"\u1091",
	        "to": ur"\u100f\u1039\u100d"
	    },
	    {
	        "from": ur"\u1092",
	        "to": ur"\u100b\u1039\u100c"
	    },
	    {
	        "from": ur"\u1019\u102c(\u107b|\u1093)",
	        "to": ur"\u1019\u1039\u1018\u102c"
	    },
	    {
	        "from": ur"(\u107b|\u1093)",
	        "to": ur"\u1039\u1018"
	    },
	    {
	        "from": ur"(\u1094|\u1095)",
	        "to": ur"\u1037"
	    },
	    {
	        "from": ur"([\u1000-\u1021])\u1037\u1032",
	        "to": ur"\1\u1032\u1037"
	    },
	    {
	        "from": ur"\u1096",
	        "to": ur"\u1039\u1010\u103d"
	    },
	    {
	        "from": ur"\u1097",
	        "to": ur"\u100b\u1039\u100b"
	    },
	    {
	    	"from": ur"\u103c([\u1000-\u1021])([\u1000-\u1021])?",
	        "to": ur"\1\u103c\2"
	    },
	    {
	        "from": ur"([\u1000-\u1021])\u103c\u103a",
	        "to": ur"\u103c\1\u103a"
	    },
	    {
	        "from": ur"\u1047(?=[\u102c-\u1030\u1032\u1036-\u1038\u103d\u1038])",
	        "to": ur"\u101b"
	    },
	    {
	        "from": ur"\u1031\u1047",
	        "to": ur"\u1031\u101b"
	    },
	    {
	        "from": ur"\u1040(\u102e|\u102f|\u102d\u102f|\u1030|\u1036|\u103d|\u103e)",
	        "to": ur"\u101d\1"
	    },
	    {
	        "from": ur"([^\u1040\u1041\u1042\u1043\u1044\u1045\u1046\u1047\u1048\u1049])\u1040\u102b",
	        "to": ur"\1\u101d\u102b"
	    },
	    {
	        "from": ur"([\u1040\u1041\u1042\u1043\u1044\u1045\u1046\u1047\u1048\u1049])\u1040\u102b(?!\u1038)",
	        "to": ur"\1\u101d\u102b"
	    },
	    {
	        "from": ur"^\u1040(?=\u102b)",
	        "to": ur"\u101d"
	    },
	    {
	        "from": ur"\u1040\u102d(?!\u0020?/)",
	        "to": ur"\u101d\u102d"
	    },
	    {
	        "from": ur"([^\u1040-\u1049])\u1040([^\u1040-\u1049\u0020]|[\u104a\u104b])",
	        "to": ur"\1\u101d\2"
	    },
	    {
	        "from": ur"([^\u1040-\u1049])\u1040(?=[\\f\\n\\r])",
	        "to": ur"\1\u101d"
	    },
	    {
	        "from": ur"([^\u1040-\u1049])\u1040$",
	        "to": ur"\1\u101d"
	    },
	    {
	        "from": ur"\u1031([\u1000-\u1021\u103f])(\u103e)?(\u103b)?",
	        "to": ur"\1\2\3\u1031"
	    },
	    {
	        "from": ur"([\u1000-\u1021])\u1031([\u103b\u103c\u103d\u103e]+)",
	        "to": ur"\1\2\u1031"
	    },
	    {
	        "from": ur"\u1032\u103d",
	        "to": ur"\u103d\u1032"
	    },
	    {
	        "from": ur"([\u102d\u102e])\u103b",
	        "to": ur"\u103b\1"
	    },
	    {
	        "from": ur"\u103d\u103b",
	        "to": ur"\u103b\u103d"
	    },
	    {
	        "from": ur"\u103a\u1037",
	        "to": ur"\u1037\u103a"
	    },
	    {
	        "from": ur"\u102f(\u102d|\u102e|\u1036|\u1037)\u102f",
	        "to": ur"\u102f\1"
	    },
	    {
	        "from": ur"(\u102f|\u1030)(\u102d|\u102e)",
	        "to": ur"\2\1"
	    },
	    {
	        "from": ur"(\u103e)(\u103b|\u103c)",
	        "to": ur"\2\1"
	    },
	    {
	        "from": ur"\u1025(?=[\u1037]?[\u103a\u102c])",
	        "to": ur"\u1009"
	    },
	    {
	        "from": ur"\u1025\u102e",
	        "to": ur"\u1026"
	    },
	    {
	        "from": ur"\u1005\u103b",
	        "to": ur"\u1008"
	    },
	    {
	        "from": ur"\u1036(\u102f|\u1030)",
	        "to": ur"\1\u1036"
	    },
	    {
	        "from": ur"\u1031\u1037\u103e",
	        "to": ur"\u103e\u1031\u1037"
	    },
	    {
	        "from": ur"\u1031\u103e\u102c",
	        "to": ur"\u103e\u1031\u102c"
	    },
	    {
	        "from": ur"\u105a",
	        "to": ur"\u102b\u103a"
	    },
	    {
	        "from": ur"\u1031\u103b\u103e",
	        "to": ur"\u103b\u103e\u1031"
	    },
	    {
	        "from": ur"(\u102d|\u102e)(\u103d|\u103e)",
	        "to": ur"\2\1"
	    },
	    {
	        "from": ur"\u102c\u1039([\u1000-\u1021])",
	        "to": ur"\u1039\1\u102c"
	    },
	    {
	        "from": ur"\u1039\u103c\u103a\u1039([\u1000-\u1021])",
	        "to": ur"\u103a\u1039\1\u103c"
	    },
	    {
	        "from": ur"\u103c\u1039([\u1000-\u1021])",
	        "to": ur"\u1039\1\u103c"
	    },
	    {
	        "from": ur"\u1036\u1039([\u1000-\u1021])",
	        "to": ur"\u1039\1\u1036"
	    },
	    {
	        "from": ur"\u104e",
	        "to": ur"\u104e\u1004\u103a\u1038"
	    },
	    {
	        "from": ur"\u1040(\u102b|\u102c|\u1036)",
	        "to": ur"\u101d\1"
	    },
	    {
	        "from": ur"\u1025\u1039",
	        "to": ur"\u1009\u1039"
	    },
	    {
	        "from": ur"([\u1000-\u1021])\u103c\u1031\u103d",
	        "to": ur"\1\u103c\u103d\u1031"
	    },
	    {
	        "from": ur"([\u1000-\u1021])\u103b\u1031\u103d(\u103e)?",
	        "to": ur"\1\u103b\u103d\2\u1031"
	    },
	    {
	        "from": ur"([\u1000-\u1021])\u103d\u1031\u103b",
	        "to": ur"\1\u103b\u103d\u1031"
	    },
	    {
	        "from": ur"([\u1000-\u1021])\u1031(\u1039[\u1000-\u1021])",
	        "to": ur"\1\2\u1031"
	    },
	    {
	        "from": ur"\u1038\u103a",
	        "to": ur"\u103a\u1038"
	    },
	    {
	        "from": ur"\u102d\u103a|\u103a\u102d",
	        "to": ur"\u102d"
	    },
	    {
	        "from": ur"\u102d\u102f\u103a",
	        "to": ur"\u102d\u102f"
	    },
	    {
	        "from": ur"\u0020\u1037",
	        "to": ur"\u1037"
	    },
	    {
	        "from": ur"\u1037\u1036",
	        "to": ur"\u1036\u1037"
	    },
	    {
	        "from": ur"[\u102d]+",
	        "to": ur"\u102d"
	    },
	    {
	        "from": ur"[\u103a]+",
	        "to": ur"\u103a"
	    },
	    {
	        "from": ur"[\u103d]+",
	        "to": ur"\u103d"
	    },
	    {
	        "from": ur"[\u1037]+",
	        "to": ur"\u1037"
	    },
	    {
	        "from": ur"[\u102e]+",
	        "to": ur"\u102e"
	    },
	    {
	        "from": ur"\u102d\u102e|\u102e\u102d",
	        "to": ur"\u102e"
	    },
	    {
	        "from": ur"\u102f\u102d",
	        "to": ur"\u102d\u102f"
	    },
	    {
	        "from": ur"\u1037\u1037",
	        "to": ur"\u1037"
	    },
	    {
	        "from": ur"\u1032\u1032",
	        "to": ur"\u1032"
	    },
	    {
	        "from": ur"\u1044\u1004\u103a\u1038",
	        "to": ur"\u104E\u1004\u103a\u1038"
	    },
	    {
	        "from": ur"([\u102d\u102e])\u1039([\u1000-\u1021])",
	        "to": ur"\u1039\2\1"
	    },
	    {
	        "from": ur"(\u103c\u1031)\u1039([\u1000-\u1021])",
	        "to": ur"\u1039\2\1"
	    },
	    {
	        "from": ur"\u1036\u103d",
	        "to": ur"\u103d\u1036"
	    }
	]
	return replace_with_rule(rule, value)


def re_sub(pattern, replacement, string):
	def _r(m):
		# Now this is ugly.
		# Python has a "feature" where unmatched groups return None
		# then re.sub chokes on this.
		# see http://bugs.python.org/issue1519638

		# this works around and hooks into the internal of the re module...

		# the match object is replaced with a wrapper that
		# returns "" instead of None for unmatched groups

		class _m():
			def __init__(self, m):
				self.m=m
				self.string=m.string
			def group(self, n):
				return m.group(n) or ""

		return re._expand(pattern, _m(m), replacement)

	return re.sub(pattern, _r, string)


def replace_with_rule(rule, value):
	if type(value) == unicode:
		data = value
	else:
		data = value.decode("utf-8")
	count = 0
	for x in rule:
		_from = x["from"]
		_to = x["to"]

		try:
			tmp = data
			data = re_sub(_from, _to, data)
			if tmp != data:
				pass
				#print(count)
		except Exception as e:
			print(e)
		finally:
			count = count + 1

	return data


if __name__ == '__main__':
	result = zg2uni("( ၉.၉.၂၀၁၉) ရက္ေန႔၊ ( ၁၉း၃၅ ) အခ်ိန္ခန္႕၊ မႏၱေလးတုိင္းေဒသႀကီး၊ ျပည္ၾကီးတံခြန္ၿမိဳ႕နယ္၊( ၇၀x၇၁ ) ေဇာ္ဂ်ီလမ္းရွိ ဆုိင္ကယ္ပစၥည္းဂုိေထာင္တြင္ မီးေလာင္မႈျဖစ္ပြားေၾကာင္း သတင္းရရွိသျဖင့္ Level 1 ယာဥ္အုပ္စုမ်ားထြက္ခြာျငွိမ္းသတ္ခဲ့ျပီး (၁၉း၄၀) အခ်ိန္တြင္ မီးျငိမ္းပါသည္။")

	with open("converted.txt", "w") as file:
		file.write(result.encode("utf-8"))
		file.close()
