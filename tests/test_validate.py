import pandas as pd

from checkcel import Checkcel
from checkcel.validators import TextValidator, DateValidator, UniqueValidator, SetValidator, IntValidator, FloatValidator, GPSValidator, EmailValidator, TimeValidator, NoValidator


class TestCheckcelValidateText():

    def test_invalid_empty(self):
        data = {'my_column': ['', 'myvalue']}
        validators = {'my_column': TextValidator()}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, empty_ok=False, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 1

    def test_valid_empty(self):
        data = {'my_column': ['', 'myvalue']}
        validators = {'my_column': TextValidator()}
        df = pd.DataFrame.from_dict(data)
        val = Checkcel(data=df, empty_ok=True, validators=validators)
        assert val.validate()

    def test_valid(self):
        data = {'my_column': ['blabla', 'myvalue']}
        validators = {'my_column': TextValidator()}
        df = pd.DataFrame.from_dict(data)
        val = Checkcel(data=df, validators=validators)
        assert val.validate()


class TestCheckcelValidateFloat():

    def test_invalid_string(self):
        data = {'my_column': ['notanumber']}
        validators = {'my_column': FloatValidator()}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, empty_ok=False, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 1

    def test_invalid_empty(self):
        data = {'my_column': ['', 6]}
        validators = {'my_column': FloatValidator()}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, empty_ok=False, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 1

    def invalid_min(self):
        data = {'my_column': [6, 4]}
        validators = {'my_column': FloatValidator(min=5)}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 1

    def invalid_max(self):
        data = {'my_column': [6, 4]}
        validators = {'my_column': FloatValidator(max=5)}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 1

    def invalid_both(self):
        data = {'my_column': [8, 6.1, 5]}
        validators = {'my_column': FloatValidator(max=7.5, min=5.5)}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 2

    def test_valid_empty(self):
        data = {'my_column': ['', 6]}
        validators = {'my_column': FloatValidator()}
        df = pd.DataFrame.from_dict(data)
        val = Checkcel(data=df, empty_ok=True, validators=validators)
        assert val.validate()

    def test_valid(self):
        data = {'my_column': [6, 4, "9.0"]}
        validators = {'my_column': FloatValidator()}
        df = pd.DataFrame.from_dict(data)
        val = Checkcel(data=df, validators=validators)
        assert val.validate()


class TestCheckcelValidateInt():

    def test_invalid_string(self):
        data = {'my_column': ['notanumber']}
        validators = {'my_column': IntValidator()}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, empty_ok=False, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 1

    def test_invalid_float(self):
        data = {'my_column': ['4.8']}
        validators = {'my_column': IntValidator()}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, empty_ok=False, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 1

    def test_invalid_empty(self):
        data = {'my_column': ['', 6]}
        validators = {'my_column': IntValidator()}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, empty_ok=False, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 1

    def invalid_min(self):
        data = {'my_column': [6, 4]}
        validators = {'my_column': IntValidator(min=5)}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 1

    def invalid_max(self):
        data = {'my_column': [6, 4]}
        validators = {'my_column': IntValidator(max=5)}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 1

    def invalid_both(self):
        data = {'my_column': [8, 6, 4]}
        validators = {'my_column': IntValidator(max=7, min=5)}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 2

    def test_valid_empty(self):
        data = {'my_column': ['', 6]}
        validators = {'my_column': IntValidator()}
        df = pd.DataFrame.from_dict(data)
        val = Checkcel(data=df, empty_ok=True, validators=validators)
        assert val.validate()

    def test_valid(self):
        data = {'my_column': [6, 4, "9"]}
        validators = {'my_column': IntValidator()}
        df = pd.DataFrame.from_dict(data)
        val = Checkcel(data=df, validators=validators)
        assert val.validate()


class TestCheckcelValidateMail():

    def test_invalid(self):
        data = {'my_column': ['invalidemail.emailprovider.com', 'invalidemail@emailprovidercom']}
        validators = {'my_column': EmailValidator()}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, empty_ok=False, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 2

    def test_invalid_empty(self):
        data = {'my_column': ['', 'validemail@emailprovider.com']}
        validators = {'my_column': EmailValidator()}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, empty_ok=False, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 1

    def test_valid_empty(self):
        data = {'my_column': ['', 'validemail@emailprovider.com']}
        validators = {'my_column': EmailValidator()}
        df = pd.DataFrame.from_dict(data)
        val = Checkcel(data=df, empty_ok=True, validators=validators)
        assert val.validate()

    def test_valid(self):
        data = {'my_column': ['validemail@emailprovider.com', 'valid2email@emailprovider.com']}
        validators = {'my_column': EmailValidator()}
        df = pd.DataFrame.from_dict(data)
        val = Checkcel(data=df, validators=validators)
        assert val.validate()


class TestCheckcelValidateDate():

    def test_invalid(self):
        data = {'my_column': ['thisisnotadate', '1991/01/1991']}
        validators = {'my_column': DateValidator()}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, empty_ok=False, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 2

    def test_invalid_empty(self):
        data = {'my_column': ['01/01/1970', '']}
        validators = {'my_column': DateValidator()}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, empty_ok=False, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 1

    def test_valid_empty(self):
        data = {'my_column': ['', '01/01/1970']}
        validators = {'my_column': DateValidator()}
        df = pd.DataFrame.from_dict(data)
        val = Checkcel(data=df, empty_ok=True, validators=validators)
        assert val.validate()

    def test_valid(self):
        data = {'my_column': ['01/01/1970', '01-01-1970', '1970/01/01', '01 01 1970']}
        validators = {'my_column': DateValidator()}
        df = pd.DataFrame.from_dict(data)
        val = Checkcel(data=df, validators=validators)
        assert val.validate()


class TestCheckcelValidateTime():

    def test_invalid(self):
        data = {'my_column': ['thisisnotatime', '248:26']}
        validators = {'my_column': TimeValidator()}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, empty_ok=False, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 2

    def test_invalid_empty(self):
        data = {'my_column': ['13h10', '']}
        validators = {'my_column': TimeValidator()}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, empty_ok=False, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 1

    def test_valid_empty(self):
        data = {'my_column': ['', '13h10']}
        validators = {'my_column': TimeValidator()}
        df = pd.DataFrame.from_dict(data)
        val = Checkcel(data=df, empty_ok=True, validators=validators)
        assert val.validate()

    def test_valid(self):
        data = {'my_column': ['13h10', '2h36PM']}
        validators = {'my_column': TimeValidator()}
        df = pd.DataFrame.from_dict(data)
        val = Checkcel(data=df, validators=validators)
        assert val.validate()


class TestCheckcelValidateUnique():

    def test_invalid(self):
        data = {'my_column': ['notunique', 'notunique']}
        validators = {'my_column': UniqueValidator()}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, empty_ok=False, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 1

    def test_invalid_empty(self):
        data = {'my_column': ['unique', '']}
        validators = {'my_column': UniqueValidator()}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, empty_ok=False, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 1

    def test_invalid_multiple(self):
        data = {'my_column': ['unique1', 'unique1'], 'another_column': ['val2', 'val2']}
        validators = {'my_column': UniqueValidator(unique_with=["another_column"]), 'another_column': NoValidator()}
        df = pd.DataFrame.from_dict(data)
        validation = Checkcel(data=df, empty_ok=False, validators=validators)
        val = validation.validate()
        assert val is False
        assert len(validation.failures['my_column']) == 1

    def test_valid_empty(self):
        data = {'my_column': ['', 'unique']}
        validators = {'my_column': UniqueValidator()}
        df = pd.DataFrame.from_dict(data)
        val = Checkcel(data=df, empty_ok=True, validators=validators)
        assert val.validate()

    def test_valid(self):
        data = {'my_column': ['unique1', 'unique2']}
        validators = {'my_column': UniqueValidator()}
        df = pd.DataFrame.from_dict(data)
        val = Checkcel(data=df, validators=validators)
        assert val.validate()

    def test_valid_multiple(self):
        data = {'my_column': ['unique1', 'unique1'], 'another_column': ['val1', 'val2']}
        validators = {'my_column': UniqueValidator(unique_with=["another_column"]), 'another_column': NoValidator()}
        df = pd.DataFrame.from_dict(data)
        val = Checkcel(data=df, validators=validators)
        assert val.validate()


class TestCheckcelValidateSet():

    def test_SetValidator(self):
        pass


class TestCheckcelValidateLinkedSet():

    def test_LinkedSetValidator(self):
        pass


class TestCheckcelValidateGPS():

    def test_GPSValidator(self):
        pass
