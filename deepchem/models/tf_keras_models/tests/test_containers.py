"""
Simple Tests for Container objects.
"""
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import unittest
from deepchem.models.tf_keras_models.graph_topology import GraphTopology
from tensorflow.python.framework import test_util

class TestContainers(test_util.TensorFlowTestCase):
  """
  Test Container usage."
  """
  def setUp(self):
    super(TestContainers, self).setUp()
    self.root = '/tmp'

  def test_graph_containers(self):
    """Simple test that Graph Container can be initialized."""
    n_atoms = 5
    n_atom_feat = 10
    batch_size = 3
    with self.test_session() as sess:
      topology = GraphTopology(n_atoms, n_atom_feat, batch_size)
      container = GraphContainer(sess, input=topology.get_inputs(),
                                 output=topology.get_nodes())