DASHBOARD = {
    "dashboard": {
        "editable": True,
        "gnetId": None,
        "graphTooltip": 0,
        "id": None,
        "iteration": 1548438780072,
        "links": [],
        "panels": [
            {
            "aliasColors": {},
            "bars": False,
            "dashLength": 10,
            "dashes": False,
            "datasource": None,
            "decimals": 2,
            "fill": 0,
            "gridPos": {
                "h": 9,
                "w": 24,
                "x": 0,
                "y": 0
            },
            "id": 2,
            "legend": {
                "alignAsTable": True,
                "avg": True,
                "current": True,
                "max": True,
                "min": True,
                "show": True,
                "total": False,
                "values": True
            },
            "lines": True,
            "linewidth": 1,
            "links": [],
            "nullPointMode": "null",
            "percentage": False,
            "pointradius": 5,
            "points": False,
            "renderer": "flot",
            "seriesOverrides": [],
            "spaceLength": 10,
            "stack": False,
            "steppedLine": False,
            "targets": [
                {
                "$$hashKey": "object:1647",
                "alias": "$tag_address",
                "groupBy": [
                    {
                    "params": [
                        "$__interval"
                    ],
                    "type": "time"
                    },
                    {
                    "params": [
                        "address"
                    ],
                    "type": "tag"
                    },
                    {
                    "params": [
                        "null"
                    ],
                    "type": "fill"
                    }
                ],
                "measurement": "ruuvitag",
                "orderByTime": "ASC",
                "policy": "default",
                "refId": "A",
                "resultFormat": "time_series",
                "select": [
                    [
                    {
                        "params": [
                        "temperature"
                        ],
                        "type": "field"
                    },
                    {
                        "params": [],
                        "type": "mean"
                    },
                    {
                        "params": [
                        "Temperature"
                        ],
                        "type": "alias"
                    }
                    ]
                ],
                "tags": [
                    {
                    "key": "address",
                    "operator": "=~",
                    "value": "/^$RuuviTag$/"
                    }
                ]
                }
            ],
            "thresholds": [],
            "timeFrom": None,
            "timeShift": None,
            "title": "Temperature",
            "tooltip": {
                "shared": True,
                "sort": 0,
                "value_type": "individual"
            },
            "type": "graph",
            "xaxis": {
                "buckets": None,
                "mode": "time",
                "name": None,
                "show": True,
                "values": []
            },
            "yaxes": [
                {
                "format": "celsius",
                "label": "",
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True
                },
                {
                "format": "short",
                "label": None,
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True
                }
            ]
            },
            {
            "aliasColors": {},
            "bars": False,
            "dashLength": 10,
            "dashes": False,
            "datasource": None,
            "decimals": 2,
            "fill": 0,
            "gridPos": {
                "h": 9,
                "w": 12,
                "x": 0,
                "y": 9
            },
            "id": 4,
            "legend": {
                "alignAsTable": True,
                "avg": True,
                "current": True,
                "max": True,
                "min": True,
                "show": True,
                "total": False,
                "values": True
            },
            "lines": True,
            "linewidth": 1,
            "links": [],
            "nullPointMode": "null",
            "percentage": False,
            "pointradius": 5,
            "points": False,
            "renderer": "flot",
            "seriesOverrides": [],
            "spaceLength": 10,
            "stack": False,
            "steppedLine": False,
            "targets": [
                {
                "$$hashKey": "object:1747",
                "alias": "$tag_address",
                "groupBy": [
                    {
                    "params": [
                        "$__interval"
                    ],
                    "type": "time"
                    },
                    {
                    "params": [
                        "address"
                    ],
                    "type": "tag"
                    },
                    {
                    "params": [
                        "null"
                    ],
                    "type": "fill"
                    }
                ],
                "measurement": "ruuvitag",
                "orderByTime": "ASC",
                "policy": "default",
                "refId": "A",
                "resultFormat": "time_series",
                "select": [
                    [
                    {
                        "params": [
                        "pressure"
                        ],
                        "type": "field"
                    },
                    {
                        "params": [],
                        "type": "mean"
                    },
                    {
                        "params": [
                        "Pressure"
                        ],
                        "type": "alias"
                    }
                    ]
                ],
                "tags": [
                    {
                    "key": "address",
                    "operator": "=~",
                    "value": "/^$RuuviTag$/"
                    }
                ]
                }
            ],
            "thresholds": [],
            "timeFrom": None,
            "timeShift": None,
            "title": "Pressure",
            "tooltip": {
                "shared": True,
                "sort": 0,
                "value_type": "individual"
            },
            "type": "graph",
            "xaxis": {
                "buckets": None,
                "mode": "time",
                "name": None,
                "show": True,
                "values": []
            },
            "yaxes": [
                {
                "format": "pressurehpa",
                "label": "",
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True
                },
                {
                "format": "short",
                "label": None,
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True
                }
            ]
            },
            {
            "aliasColors": {},
            "bars": False,
            "dashLength": 10,
            "dashes": False,
            "datasource": None,
            "decimals": 2,
            "fill": 0,
            "gridPos": {
                "h": 9,
                "w": 12,
                "x": 12,
                "y": 9
            },
            "id": 3,
            "legend": {
                "alignAsTable": True,
                "avg": True,
                "current": True,
                "max": True,
                "min": True,
                "show": True,
                "total": False,
                "values": True
            },
            "lines": True,
            "linewidth": 1,
            "links": [],
            "nullPointMode": "null",
            "percentage": False,
            "pointradius": 5,
            "points": False,
            "renderer": "flot",
            "seriesOverrides": [],
            "spaceLength": 10,
            "stack": False,
            "steppedLine": False,
            "targets": [
                {
                "$$hashKey": "object:1847",
                "alias": "$tag_address",
                "groupBy": [
                    {
                    "params": [
                        "$__interval"
                    ],
                    "type": "time"
                    },
                    {
                    "params": [
                        "address"
                    ],
                    "type": "tag"
                    },
                    {
                    "params": [
                        "null"
                    ],
                    "type": "fill"
                    }
                ],
                "measurement": "ruuvitag",
                "orderByTime": "ASC",
                "policy": "default",
                "refId": "A",
                "resultFormat": "time_series",
                "select": [
                    [
                    {
                        "params": [
                        "humidity"
                        ],
                        "type": "field"
                    },
                    {
                        "params": [],
                        "type": "mean"
                    },
                    {
                        "params": [
                        "Humidity"
                        ],
                        "type": "alias"
                    }
                    ]
                ],
                "tags": [
                    {
                    "key": "address",
                    "operator": "=~",
                    "value": "/^$RuuviTag$/"
                    }
                ]
                }
            ],
            "thresholds": [],
            "timeFrom": None,
            "timeShift": None,
            "title": "Humidity",
            "tooltip": {
                "shared": True,
                "sort": 0,
                "value_type": "individual"
            },
            "type": "graph",
            "xaxis": {
                "buckets": None,
                "mode": "time",
                "name": None,
                "show": True,
                "values": []
            },
            "yaxes": [
                {
                "format": "percent",
                "label": "",
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True
                },
                {
                "format": "short",
                "label": None,
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True
                }
            ]
            },
            {
            "aliasColors": {},
            "bars": False,
            "dashLength": 10,
            "dashes": False,
            "datasource": None,
            "decimals": 3,
            "fill": 0,
            "gridPos": {
                "h": 9,
                "w": 12,
                "x": 0,
                "y": 18
            },
            "id": 5,
            "legend": {
                "alignAsTable": True,
                "avg": True,
                "current": True,
                "max": True,
                "min": True,
                "show": True,
                "total": False,
                "values": True
            },
            "lines": True,
            "linewidth": 1,
            "links": [],
            "nullPointMode": "null",
            "percentage": False,
            "pointradius": 5,
            "points": False,
            "renderer": "flot",
            "seriesOverrides": [],
            "spaceLength": 10,
            "stack": False,
            "steppedLine": False,
            "targets": [
                {
                "$$hashKey": "object:1947",
                "alias": "$tag_address",
                "groupBy": [
                    {
                    "params": [
                        "$__interval"
                    ],
                    "type": "time"
                    },
                    {
                    "params": [
                        "address"
                    ],
                    "type": "tag"
                    },
                    {
                    "params": [
                        "null"
                    ],
                    "type": "fill"
                    }
                ],
                "measurement": "ruuvitag",
                "orderByTime": "ASC",
                "policy": "default",
                "refId": "A",
                "resultFormat": "time_series",
                "select": [
                    [
                    {
                        "params": [
                        "battery_voltage"
                        ],
                        "type": "field"
                    },
                    {
                        "params": [],
                        "type": "mean"
                    },
                    {
                        "params": [
                        "Battery voltage"
                        ],
                        "type": "alias"
                    }
                    ]
                ],
                "tags": [
                    {
                    "key": "address",
                    "operator": "=~",
                    "value": "/^$RuuviTag$/"
                    }
                ]
                }
            ],
            "thresholds": [],
            "timeFrom": None,
            "timeShift": None,
            "title": "Battery voltage",
            "tooltip": {
                "shared": True,
                "sort": 0,
                "value_type": "individual"
            },
            "type": "graph",
            "xaxis": {
                "buckets": None,
                "mode": "time",
                "name": None,
                "show": True,
                "values": []
            },
            "yaxes": [
                {
                "format": "volt",
                "label": "",
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True
                },
                {
                "format": "short",
                "label": None,
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True
                }
            ]
            },
            {
            "aliasColors": {},
            "bars": False,
            "dashLength": 10,
            "dashes": False,
            "datasource": None,
            "decimals": 3,
            "fill": 0,
            "gridPos": {
                "h": 9,
                "w": 12,
                "x": 12,
                "y": 18
            },
            "id": 6,
            "legend": {
                "alignAsTable": True,
                "avg": True,
                "current": True,
                "max": True,
                "min": True,
                "show": True,
                "total": False,
                "values": True
            },
            "lines": True,
            "linewidth": 1,
            "links": [],
            "nullPointMode": "null",
            "percentage": False,
            "pointradius": 5,
            "points": False,
            "renderer": "flot",
            "seriesOverrides": [],
            "spaceLength": 10,
            "stack": False,
            "steppedLine": False,
            "targets": [
                {
                "$$hashKey": "object:1437",
                "alias": "$tag_address",
                "groupBy": [
                    {
                    "params": [
                        "$__interval"
                    ],
                    "type": "time"
                    },
                    {
                    "params": [
                        "address"
                    ],
                    "type": "tag"
                    },
                    {
                    "params": [
                        "null"
                    ],
                    "type": "fill"
                    }
                ],
                "measurement": "ruuvitag",
                "orderByTime": "ASC",
                "policy": "default",
                "refId": "A",
                "resultFormat": "time_series",
                "select": [
                    [
                    {
                        "params": [
                        "tx_power"
                        ],
                        "type": "field"
                    },
                    {
                        "params": [],
                        "type": "mean"
                    },
                    {
                        "params": [
                        "Transmit power"
                        ],
                        "type": "alias"
                    }
                    ]
                ],
                "tags": [
                    {
                    "key": "address",
                    "operator": "=~",
                    "value": "/^$RuuviTag$/"
                    }
                ]
                }
            ],
            "thresholds": [],
            "timeFrom": None,
            "timeShift": None,
            "title": "Transmit power",
            "tooltip": {
                "shared": True,
                "sort": 0,
                "value_type": "individual"
            },
            "type": "graph",
            "xaxis": {
                "buckets": None,
                "mode": "time",
                "name": None,
                "show": True,
                "values": []
            },
            "yaxes": [
                {
                "$$hashKey": "object:1500",
                "format": "dBm",
                "label": "",
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True
                },
                {
                "$$hashKey": "object:1501",
                "format": "short",
                "label": None,
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True
                }
            ]
            }
        ],
        "refresh": "5s",
        "schemaVersion": 16,
        "style": "dark",
        "tags": [],
        "templating": {
            "list": [
            {
                "allValue": None,
                "current": {
                "tags": [],
                "text": "All",
                "value": [
                    "$__all"
                ]
                },
                "datasource": "influx",
                "hide": 0,
                "includeAll": True,
                "label": None,
                "multi": True,
                "name": "RuuviTag",
                "options": [],
                "query": "SHOW TAG VALUES ON \"ruuvitag\" WITH KEY = \"address\"",
                "refresh": 1,
                "regex": "",
                "sort": 0,
                "tagValuesQuery": "",
                "tags": [],
                "tagsQuery": "",
                "type": "query",
                "useTags": False
            }
            ]
        },
        "time": {
            "from": "now-5m",
            "to": "now"
        },
        "timepicker": {
            "refresh_intervals": [
            "5s",
            "10s",
            "30s",
            "1m",
            "5m",
            "15m",
            "30m",
            "1h",
            "2h",
            "1d"
            ],
            "time_options": [
            "5m",
            "15m",
            "1h",
            "6h",
            "12h",
            "24h",
            "2d",
            "7d",
            "30d"
            ]
        },
        "timezone": "",
        "title": "RuuviTag",
        "uid": "RuuviTag",
        "version": 4,
    },
}
