# Copyright (c) 2012 sun-exploit <a1@sun-exploit.com>
#
#  This file is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import sys
from modules.component.pcs_component import pcs_component
#####################################################################
# Bootstrapping
#####################################################################
def start():
    """Main entry point into the configuration client"""

    # Test
    hello_world()
    c = pcs_component()

#####################################################################
# Functions
#####################################################################
def hello_world():
        print "hello_world from {0}".format(__name__)

