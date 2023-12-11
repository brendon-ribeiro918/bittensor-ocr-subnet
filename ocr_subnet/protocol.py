# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# TODO(developer): Set your name
# Copyright © 2023 <your name>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import typing
import bittensor as bt


class OCRSynapse(bt.Synapse):
    """
    A simple OCR synapse protocol representation which uses bt.Synapse as its base.
    This protocol enables communication betweenthe miner and the validator.

    Attributes:
    - image: A pdf image to be processed by the miner.
    - response: List[dict] containing data extracted from the image.
    """

    # Required request input, filled by sending dendrite caller. It is a base64 encoded string.
    base64_image: str

    # Optional request output, filled by recieving axon.
    response: typing.Optional[typing.List[dict]] = None

    def deserialize(self) -> int:
        """
        Deserialize the miner response. This method retrieves the response from
        the miner in the form of `response`, maybe this also takes care of casting it to List[dict]?

        Returns:
        - List[dict: The deserialized response, which is a list of dictionaries containing the extracted data.
        """
        return self.response
