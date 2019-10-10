class SecurionPayException(Exception):
    def __init__(self, type, code, message, charge_id, blacklist_rule_id):
        self.type = type
        self.code = code
        self.message = message
        self.charge_id = charge_id
        self.blacklist_rule_id = blacklist_rule_id

    def __str__(self):
        return (
            "SecurionPayException:\n\tType: %s\n\tCode: %s\n\tMessage: %s\n\tChargeId: %s\n\tBlacklistRuleId: %s"
            % tuple(
                [
                    str(v)
                    for v in [
                        self.type,
                        self.code,
                        self.message,
                        self.charge_id,
                        self.blacklist_rule_id,
                    ]
                ]
            )
        )
